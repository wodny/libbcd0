#    Copyright 2011  Marcin Szewczyk <Marcin.Szewczyk@wodny.org>
#
#    This file is part of libbcd.
#
#    Libbcd is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Libbcd is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with libbcd.  If not, see <http://www.gnu.org/licenses/>.


import hivex
from mappings import *

class BCD:
    tab = "    "

    def __init__(self, filename):
        self.filename = filename
        self.hivex = hivex.Hivex(filename, write=True)

    def commit(self):
        self.hivex.commit(self.filename)

    def root(self):
        return self.hivex.root()

    def print_tree(self, node, level = 0):
        name_id = self.hivex.node_name(node)
        if name_id.startswith('{') and name_id.endswith('}'):
            try:
                name = guid_to_name[name_id.lower()[1:-1]]
            except (KeyError):
                name = name_id
        else:
            try:
                name_id = int("0x{0}".format(name_id), 16)
                name = id_to_name[name_id]
            except (KeyError, ValueError):
                name = name_id

        values = self.hivex.node_values(node)
        children = self.hivex.node_children(node)

        print("{0}\-- {1}".format(BCD.tab * level, name))
        if values:
            #print("{0}  Values:".format(BCD.tab * level))
            for value_id in values:
                key = self.hivex.value_key(value_id)
                value = self.hivex.value_type(value_id)
                vtype = self.hivex.value_type(value_id)[0]
                if vtype == 1:
                    value = self.hivex.value_string(value_id)
                if vtype == 4 and key == "Type":
                    value = BCD.decode_type(self.hivex.value_dword(value_id))
#                if name == "BcdLibraryDevice_ApplicationDevice" or \
#                   name == "BcdOSLoaderDevice_OSDevice":
#                    print(self.hivex.value_value(value_id))
                print("{0}    * {1} = {2}".format(BCD.tab * level, key, value))

        for node in children:
            self.print_tree(node, level + 1)

    def __node_by_name(self, node, name):
        for child in self.hivex.node_children(node):
            if self.hivex.node_name(child) == name:
                return child

    def node_by_path(self, path):
        name_frags = path.split('/')
        node = self.hivex.root()
        for name_frag in name_frags:
            node = self.__node_by_name(node, name_frag)
            if node is None:
                break
        return node
    
    @staticmethod
    def decode_type(dword):
        otype = (0xF0000000 & dword) >> 28 
        if otype == 1:
            itype = (0x00F00000 & dword) >> 20
            try:
                itype_s = id_to_imagetype[itype]
            except KeyError:
                itype_s = "Unknown"
    
            atype = 0xFFFFF & dword
            try:
                atype_s = id_to_apptype[atype]
            except KeyError:
                atype_s = "Unknown"
    
            return ("Application", itype_s, atype_s)
        if otype == 2:
            return ("Inherited", None, None)
        if otype == 3:
            return ("Device", None, None)
        return ("Unknown", None, None)

    def get_object_by_guid(self, guid):
        return self.node_by_path("Objects/{0}".format(guid))

    def get_element(self, node):
        return self.hivex.node_get_value(node, "Element")

    def get_elemnode_by_spec(self, guid, elementtype):
        return self.node_by_path("Objects/{0}/Elements/{1}".format(
            guid,
            hex(name_to_id[elementtype])[2:]
        ))

    def get_element_by_spec(self, guid, elementtype):
        return self.get_element(self.get_elemnode_by_spec(guid, elementtype))

    @staticmethod
    def value_to_dict(name, value):
        return {
            "key": name,
            "value": value[1],
            "t": value[0]
        }

    @staticmethod
    def element_to_dict(value):
        return BCD.value_to_dict("Element", value)
