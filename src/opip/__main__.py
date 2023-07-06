import sys
import pip

def install(package_name):
    pip.main(['install', package_name])

# def upgrade(package_name):
#     pip.main(['install', package_name, '--upgrade'])

def uninstall(package_name):
    pip.main(['uninstall', package_name])

def main():
    # for i in range(len(sys.argv)-1):
    #     print(sys.argv[i+1])
    command = sys.argv[1]
    package_name = sys.argv[2]

    if command == 'install':
        install(package_name)
    # elif command == 'upgrade':
    #     upgrade(package_name)
    elif command == 'uninstall':
        uninstall(package_name)

if __name__ == "__main__" :
    main()

    
