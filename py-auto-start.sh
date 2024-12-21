import libvirt

def main():
    conn = libvirt.open('qemu:///system')
    if conn is None:
        print('Failed to open connection to qemu:///system')
        return

    domain_names = conn.listAllDomains()

    for domain in domain_names:
        name = domain.name()
        autostart = domain.autostart()
        print(f"{name} auto: {autostart}")
        if autostart:
            try:
                domain.create()
            except libvirt.libvirtError as e:
                print(f"{name} start failed: {e}")
    conn.close()

if __name__ == '__main__':
    main()

