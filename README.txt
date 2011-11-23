Library
-------
This library can be used to edit the Windows `Boot Configuration Data`_ 
(BCD). For example one can add a new entry in the Windows Vista/7 
bootloader menu.


Assumptions
-----------
The script below assumes that there will be a file called "linux.bin" on 
the same partition Windows was installed to. Usually it's C: -- the one 
with the Windows directory, not the one with the BCD file.

That "linux.bin" file is an MBR image. It can be created using the 
following command:

::

  install-mbr -t 1 -T /dev/sda -p 3 -f /media/sda2/linux.bin

The ``install-mbr`` command comes with the `mbr package`_ from Debian 
repositories.

Those particular parameters mean:
  * timeout is 1 second,
  * take partitions layout from the real /dev/sda MBR,
  * Linux bootloader is at partition 3 (/dev/sda3),
  * Windows partition is mounted at /media/sda2.

Issue that command after installing Linux or at least after creating 
a new partition layout.

Booting process
---------------

::

  BIOS → MBR at /dev/sda → Windows bootloader →
  artificial MBR in linux.bin → Linux bootloader → kernel

Example
-------

The example below adds a new BCD entry to boot Linux. The entry will be 
named "My Linux".

Execute it like that:

::

  ./example.py <path_to_the_BCD_file>

And the script:

::

    #!/usr/bin/python
    
    import uuid
    import sys
    
    from lib.mappings import *
    from lib.BCD import BCD
    from lib.BCDMenu import BCDMenu, BCDBootEntry
    
    class BCDMyLinuxUpdater(object):
        mylinux_desc  = "My Linux"
        mylinux_image = "\\linux.bin"
        menu_timeout = 20
    
        def __init__(self, filename):
            self.__bcdmenu = BCDMenu(filename)
    
        def __create_mylinux(self):
            guid = "{{{0}}}".format(uuid.uuid1())
            print("New GUID: {0}".format(guid))
            entry = BCDBootEntry(self.__bcdmenu.bcd, guid)
            entry.description = BCDMyLinuxUpdater.mylinux_desc
            win7 = self.__bcdmenu.find_bootentry_by_name("Windows 7")
            entry.boot_device = win7.boot_device
            entry.applicationpath = BCDMyLinuxUpdater.mylinux_image
            return entry
    
        def update(self):
            mylinux = self.__bcdmenu.find_bootentry_by_name(BCDMyLinuxUpdater.mylinux_desc)
            if mylinux is not None:
                self.__bcdmenu.delete_entry(mylinux)
            mylinux = self.__create_mylinux()
            self.__bcdmenu.add_entry(mylinux)
            self.__bcdmenu.timeout = BCDMyLinuxUpdater.menu_timeout
            self.__bcdmenu.commit()
    
        def print_info(self):
            print("BCD information:")
            print("Timeout: {0}".format(self.__bcdmenu.timeout))
            print("Active boot entries:")
            for element in self.__bcdmenu.bootentries:
                print("  {0}".format(element.description))
                print("    {0}".format(element.guid))
    
    if __name__ == "__main__":
        if len(sys.argv) != 2:
            exit("Hive filename required.")
    
        filename = sys.argv[1]
    
        mylinux = BCDMyLinuxUpdater(filename)
        print("Before changes:")
        mylinux.print_info()
        print("")
        mylinux.update()
        print("")
        print("After changes:")
        mylinux.print_info()


Unknown
-------
That code assumes that the "linux.bin" file is on the Windows partition, 
so `BcdLibraryDevice_ApplicationDevice`_ (``11000001``) is just copied 
from the Windows 7 entry.

That element's structure hasn't been decoded yet. It has been tested 
that at offset 0x20 there is the byte offset of the system partition and 
at offset 0x38 there is the disk signature from the MBR (offset 0x1B8).

But it is still unknown what do some bytes do:
  * 0x06 at 0x10,
  * 0x48 at 0x18,
  * 0x01 at 0x34.

Example hex dump
----------------

::

  0x00:    00,00,00,00,  00,00,00,00,  00,00,00,00,  00,00,00,00,
  0x10:    06,00,00,00,  00,00,00,00,
  0x18:    48,00,00,00,  00,00,00,00,
  0x20:    00,00,50,06,  00,00,00,00,  00,00,00,00,  00,00,00,00,
  0x30:    00,00,00,00,
  0x34:    01,00,00,00,
  0x38:    11,fb,ac,fd,  00,00,00,00,  00,00,00,00,  00,00,00,00,
  0x48:    00,00,00,00,  00,00,00,00,  00,00,00,00,  00,00,00,00

Partition offset: ``00,00,50,06 == 0x06500000 == 105906176 bytes == 206848 sectors * 512 bytes``.

Disk signature: ``11fbacfd``.

For MBR containing the following layout:

::

  partition 1: ID=0x7,  starthead 32,  startsector 2048,      204800    sectors
  partition 2: ID=0x7,  starthead 223, startsector 206848,    522535222 sectors
  partition 3: ID=0xb,  starthead 254, startsector 522755100, 4192965   sectors
  partition 4: ID=0x83, starthead 254, startsector 526948065, 4192965   sectors





.. _`Boot Configuration Data`: http://msdn.microsoft.com/en-us/windows/hardware/gg463059
.. _`mbr package`: http://packages.debian.org/squeeze/mbr
.. _`BcdLibraryDevice_ApplicationDevice`: http://msdn.microsoft.com/en-us/library/dd405459%28v=VS.85%29.aspx


.. vi: ft=rst
