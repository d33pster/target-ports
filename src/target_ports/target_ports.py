#!/usr/bin/env python3

__version__ = '1.0.7'

from socket import socket, AF_INET, SOCK_STREAM, gaierror, error, setdefaulttimeout
from optioner import options
from sys import argv
from re import match
import termcolor

class _scan_ports_:
    def __init__(self, targets:str | list[str], nports: int = 65535):
        """_scan_ports_:
        Scan ports on a target.

        Args:
            targets (str | list[str]): target ip
            nports (int, optional): Number of ports to scan. Defaults to 65535.
        """
        # print logo
        print(termcolor.colored('target-ports', 'blue'), termcolor.colored(f'v{__version__}', 'red'), 'Jumpstart')
        
        # define a container
        self.container = []
        
        # call scan according to targets
        if type(targets)==str:
            self.scan(targets, nports)
            if len(self.container)==0:
                print('|-- No Ports Opened for', termcolor.colored(f'{targets}', 'red'))
                self.container = []
        elif type(targets)==list[str]:
            print(termcolor.colored((f'|-- Multiple Targets Detected.'), 'blue'))
            for target in targets:
                self.scan(target, nports)
                if len(self.container)==0:
                    print('|-- No Ports Opened for', termcolor.colored(f'{target}', 'red'))
                    self.container = []
    
    def scan(self, target:str, ports: int):
        print('|-- Starting scan for', termcolor.colored(f'{target}.', 'red'))
        for port in range(1, ports+1):
            self.scanport(target, port)
    
    def scanport(self, target:str, port: int):
        try:
            sock = socket(AF_INET, SOCK_STREAM)
            setdefaulttimeout(2.5)
            s = sock.connect_ex((target, port))
            if s==0:
                print(termcolor.colored((f'[+] Port {port} is opened.'), 'green'))
                self.container.append(port)
            else:
                print(termcolor.colored(f'[-] port {port} is closed.', 'yellow'), end='\r')
            sock.close()
        except KeyboardInterrupt:
            exit(1)
        except gaierror:
            print(termcolor.colored('SCANERROR', 'red'), f' : cannot resolve {target}.')
            exit(1)
        except error:
            print(termcolor.colored('SCANERROR', 'red'), f' : {target} did not respond.')
            exit(1)

def version():
    print(termcolor.colored('target-ports', 'blue'))
    print(termcolor.colored(f'            version v{__version__}', 'red'))
    print('            author: d33pster, GitHub: @d33pster')
    exit(0)

def helper():
    print(termcolor.colored('target-ports', 'blue'), termcolor.colored(f'v{__version__}', 'red'))
    print('\nhelp text\n')
    print('  |  -h or --help      : show this help text and exit.')
    print('  |  -v or --version   : show version and exit.')
    print('  |  -c or --current   : scan localhost.')
    print('  |  -t or --target    : specify single target.')
    print('  |  -ts or --targets  : specify multiple targets.')
    print('  |  -p or --ports     : number of ports to scan (each, if more than one target is provided.)[optional: default -> 65535]')
    print(termcolor.colored('\nNote', 'red') + ':')
    print('     (i) -t(or --target) and -ts(or --targets) are mutually exclusive.')
    print('    (ii) -p(or --ports) is optional.')
    print('   (iii) This tool is just for educational pursose. The author(s) are not responsible for any misuse (AS STATED IN THE LICENSE).')
    exit(0)

def main():
    # args
    shortargs = ['h', 'v', 't', 'ts', 'p','c']
    longargs = ['help', 'version', 'target', 'targets', 'ports','current']
    
    optionctrl = options(shortargs, longargs, argv[1:], compulsory_short_args=['t'], compulsory_long_args=['target'], ignore=['-h', '--help', '-v', '--version', '-ts', '--targets', '-c', '--current'], ifthisthennotthat=[['h','help'],['v','version'], ['t','target'],['ts','targets']])
    
    args, check, error, falseargs = optionctrl._argparse()
    
    ports = 65535
    target: str | list[str]
    current:bool = False
    
    if not check:
        print(termcolor.colored(('SCANERROR'), 'red'), f': {error}')
        exit(1)
    else:
        # check version and help
        if '-v' in args or '--version' in args:
            version()
        
        if '-h' in args or '--help' in args:
            helper()
        
        if '-c' in args or '--current' in args:
            current = True
        
        # check ports
        if '-p' in args:
            ports = optionctrl._what_is_('p')
        elif '--ports' in args:
            ports = optionctrl._what_is_('ports')
        else:
            pass
        
        # check for single target
        if '-t' in args:
            target = optionctrl._what_is_('t')
        elif '--target' in args:
            target = optionctrl._what_is_('target')
        else:
            pass
        
        # check for multiple targets
        if '-ts' in args:
            index1=0
            index2=0
            length = 0
            for i in range(len(argv)):
                if argv[i] == '-ts':
                    index1 = i
                    for j in range(i+1, len(argv)):
                        if match('^-\w+$', argv[j]):
                            index2 = j
            
            length = index2-index1-1
            if index2==0:
                length = len(argv[(index1+1):])

            target = list(optionctrl._what_is_('ts', length))
        elif '--targets' in args:
            index1=0
            index2=0
            length = 0
            for i in range(len(argv)):
                if argv[i] == '-ts':
                    index1 = i
                    for j in range(i+1, len(argv)):
                        if match('^-\w+$', argv[j]):
                            index2 = j
            
            length = index2-index1-1
            if index2==0:
                length = len(argv[(index1+1):])

            target = list(optionctrl._what_is_('targets', length))
        else:
            pass
    
    # class obj
    if not current:
        scanctrl = _scan_ports_(target, int(ports))
    else:
        scanctrl = _scan_ports_('127.0.0.1', int(ports))

if __name__=='__main__':
    main()