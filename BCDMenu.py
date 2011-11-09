import struct
from BCD import BCD

class BCDMenu(object):
    def __init__(self, filename):
        self.bcd = BCD(filename)

    def commit(self):
        self.bcd.commit()

    @property
    def timeout(self):
        timeout_elem = self.bcd.get_element_by_spec(
            "{9dea862c-5cdd-4e70-acc1-f32b344d4795}",
            "BcdBootMgrInteger_Timeout"
        )
        return struct.unpack("<q", self.bcd.hivex.value_value(timeout_elem)[1])[0]

    @timeout.setter
    def timeout(self, value):
        timeout_node = self.bcd.get_elemnode_by_spec(
            "{9dea862c-5cdd-4e70-acc1-f32b344d4795}",
            "BcdBootMgrInteger_Timeout"
        )
        timeout_enc = struct.pack("<q", value)
        value_s = BCD.element_to_dict((3, timeout_enc))
        self.bcd.hivex.node_set_value(timeout_node, value_s)

    def __bootentriesguids(self):
        disporder_elem = self.bcd.get_element_by_spec(
            "{9dea862c-5cdd-4e70-acc1-f32b344d4795}",
            "BcdBootMgrObjectList_DisplayOrder"
        )
        return self.bcd.hivex.value_multiple_strings(disporder_elem)

    @property
    def bootentries(self):
        # TODO: Make it search all entries, not only active ones
        self.cleanup_entries()
        guids = self.__bootentriesguids()
        return  [ BCDBootEntry(self.bcd, guid) for guid in guids ]

    @bootentries.setter
    def bootentries(self, entries):
        guids = [ entry.guid for entry in entries ]
        guids_hex = "\x00".join(guids) + "\x00\x00"
        guids_hex = guids_hex.encode("utf-16le")

        disporder_node = self.bcd.get_elemnode_by_spec(
            "{9dea862c-5cdd-4e70-acc1-f32b344d4795}",
            "BcdBootMgrObjectList_DisplayOrder"
        )
        value_s = BCD.element_to_dict((7, guids_hex))
        self.bcd.hivex.node_set_value(disporder_node, value_s)

    def cleanup_entries(self):
        guids = self.__bootentriesguids()
        guids_existing = [ guid for guid in guids if self.bcd.get_object_by_guid(guid) ]
        self.bootentries = [ BCDBootEntry(self.bcd, guid) for guid in guids_existing ]

    def find_bootentry_by_name(self, name):
        for element in self.bootentries:
            if element.description == name:
                return element

    def delete_entry(self, entry):
        node = self.bcd.get_object_by_guid(entry.guid)
        self.bcd.hivex.node_delete_child(node)
        self.cleanup_entries()

    def add_entry(self, entry):
        guids = self.bootentries
        guids.append(entry)
        self.bootentries = guids
        

class BCDBootEntry(object):
    def __init__(self, bcd, guid):
        self.__bcd = bcd
        self.guid = guid
        self.__ensure_skeleton()

    def __ensure_skeleton(self):
        object = self.__bcd.get_object_by_guid(self.guid)
        if object is None:
            objects_node = self.__bcd.node_by_path("Objects")
            object_node = self.__bcd.hivex.node_add_child(objects_node, self.guid)

            desc_node = self.__bcd.hivex.node_add_child(object_node, "Description")
            value_s = BCD.value_to_dict("Type", (4, "\x08\x00\x40\x10"))
            self.__bcd.hivex.node_set_value(desc_node, value_s)
            
            elems_node = self.__bcd.hivex.node_add_child(object_node, "Elements")
            self.__bcd.hivex.node_add_child(elems_node, "11000001")
            self.__bcd.hivex.node_add_child(elems_node, "12000002")
            self.__bcd.hivex.node_add_child(elems_node, "12000004")


    def __get_description_node(self):
        return self.__bcd.get_elemnode_by_spec(self.guid, "BcdLibraryString_Description")

    @property
    def description(self):
        elem = self.__bcd.get_element(self.__get_description_node())
        return self.__bcd.hivex.value_string(elem)

    @description.setter
    def description(self, desc):
        desc_node = self.__get_description_node()
        value_s = BCD.element_to_dict((1, desc.encode("utf-16le")))
        self.__bcd.hivex.node_set_value(desc_node, value_s)

    def __get_applicationpath_node(self):
        return self.__bcd.get_elemnode_by_spec(self.guid, "BcdLibraryString_ApplicationPath")

    @property
    def applicationpath(self):
        elem = self.__bcd.get_element(self.__get_applicationpath_node())
        return self.__bcd.hivex.value_string(elem)

    @applicationpath.setter
    def applicationpath(self, path):
        path_node = self.__get_applicationpath_node()
        value_s = BCD.element_to_dict((1, path.encode("utf-16le")))
        self.__bcd.hivex.node_set_value(path_node, value_s)

    def __get_appdevice_node(self):
        return self.__bcd.get_elemnode_by_spec(
            self.guid,
            "BcdLibraryDevice_ApplicationDevice"
        )
 
    @property
    def boot_device(self):
        element = self.__bcd.get_element(self.__get_appdevice_node())
        return self.__bcd.hivex.value_value(element)

    @boot_device.setter
    def boot_device(self, value):
        node = self.__get_appdevice_node()
        value_s = BCD.element_to_dict(value)
        self.__bcd.hivex.node_set_value(node, value_s)
