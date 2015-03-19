
import os

class Driver(object):
    
    url_base = "/sys/class/gpio/"
    
    class DIR():
        L = 'out'
        H = 'in'
        def __getitem__(cls,itemname):
            return {'L':'out', 'H':'in'}[itemname]
        def __repr__(self):
            return "{'L':'out', 'H':'in'}"
        
    class DRIVE():
        L = 'pulldown'
        H = 'pullup'
        def __getitem__(cls,itemname):
            return {'L':'pulldown', 'H':'pullup'}[itemname]
        def __repr__(self):
            return "{'L':'pulldown', 'H':'pullup'}"
            
    galileo_gen2_map = {'IO0': {'linux':'gpio11', 'level':'gpio32', 'pull':'gpio33', 'mux1':'-','mux2':'-', 'interrupt':'L/H/R/F'},
                        'IO1': {'linux':'gpio12', 'level':'gpio28', 'pull':'gpio29', 'mux1':'gpio45(L)','mux2':'-', 'interrupt':'L/H/R/F'},
                        'IO2': {'linux':'gpio13', 'level':'gpio34', 'pull':'gpio35', 'mux1':'gpio77(L)','mux2':'-', 'interrupt':'L/H/R/F'},
                        'NaN': {'linux':'gpio61', 'level':'-', 'pull':'gpio35', 'mux1':'gpio77(L)','mux2':'-', 'interrupt':'R/F/B'},
                        'IO3': {'linux':'gpio14', 'level':'gpio16', 'pull':'gpio17', 'mux1':'gpio76(L)','mux2':'gpio64(L)', 'interrupt':'L/H/R/F'},
                        'IO3': {'linux':'gpio62', 'level':'-', 'pull':'gpio17', 'mux1':'gpio76(L)','mux2':'gpio64(L)', 'interrupt':'R/F/B'},
                        'IO4': {'linux':'gpio6', 'level':'gpio36', 'pull':'gpio37', 'mux1':'-','mux2':'-', 'interrupt':'R/F/B'},
                        'IO5': {'linux':'gpio0', 'level':'gpio18', 'pull':'gpio19', 'mux1':'gpio66(L)','mux2':'-', 'interrupt':'R/F/B'},
                        'IO6': {'linux':'gpio1', 'level':'gpio20', 'pull':'gpio21', 'mux1':'gpio68(L)','mux2':'-', 'interrupt':'R/F/B'},
                        'IO7': {'linux':'gpio38', 'level':'-', 'pull':'gpio39', 'mux1':'-','mux2':'-', 'interrupt':'-'},
                        'IO8': {'linux':'gpio40', 'level':'-', 'pull':'gpio41', 'mux1':'-','mux2':'-', 'interrupt':'-'},
                        'IO9': {'linux':'gpio4', 'level':'gpio22', 'pull':'gpio23', 'mux1':'gpio70(L)','mux2':'-', 'interrupt':'R/F/B'},
                        'IO10': {'linux':'gpio10', 'level':'gpio26', 'pull':'gpio27', 'mux1':'gpio74(L)','mux2':'-', 'interrupt':'L/H/R/F'},
                        'IO11': {'linux':'gpio5', 'level':'gpio24', 'pull':'gpio25', 'mux1':'gpio44(L)','mux2':'gpio72(L)', 'interrupt':'R/F/B'},
                        'IO12': {'linux':'gpio15', 'level':'gpio42', 'pull':'gpio43', 'mux1':'-','mux2':'-', 'interrupt':'L/H/R/F'},
                        'IO13': {'linux':'gpio7', 'level':'gpio30', 'pull':'gpio31', 'mux1':'gpio46(L)','mux2':'-', 'interrupt':'R/F/B'},
                        'IO14': {'linux':'gpio48', 'level':'-', 'pull':'gpio49', 'mux1':'-','mux2':'-', 'interrupt':'R/F/B'},
                        'IO15': {'linux':'gpio50', 'level':'-', 'pull':'gpio51', 'mux1':'-','mux2':'-', 'interrupt':'R/F/B'},
                        'IO16': {'linux':'gpio52', 'level':'-', 'pull':'gpio53', 'mux1':'-','mux2':'-', 'interrupt':'R/F/B'},
                        'IO17': {'linux':'gpio54', 'level':'-', 'pull':'gpio55', 'mux1':'-','mux2':'-', 'interrupt':'R/F/B'},
                        'IO18': {'linux':'gpio56', 'level':'-', 'pull':'gpio57', 'mux1':'gpio60(H)','mux2':'gpio78(H)', 'interrupt':'R/F/B'},
                        'IO19': {'linux':'gpio58', 'level':'-', 'pull':'gpio59', 'mux1':'gpio60(H)','mux2':'gpio79(H)', 'interrupt':'R/F/B'}}

    def __init__(self):
        self.export = self.url_base+"export"
    
    def chmod(self,uri,permissions):
        os.chmod(uri,permissions)
    
    def find_gpio(self, pin, fields=["linux","level","pull"]):
        lista = lambda name: self.galileo_gen2_map['IO'+str(pin)][name]        
        dicc = {}
        for name in fields:
            lista2 = lista(name)
            if type(lista2)==str:
                dicc[name] = lista(name)
            else:
                dicc[name] = list(lista(name))[0]
        return dicc
    
    def config_gpio(self,gpio,dir=None,drive=None):
        step2 = self.url_base+gpio+"/direction"
        step3 = self.url_base+gpio+"/drive"
        with open(self.export,'w+') as fd:
            fd.write(gpio[4:])
        if dir:
            with open(step2,'w+') as fd:
                fd.write(dir)
        if drive:
            with open(step3,'w+') as fd:
                fd.write(drive)

    def write_gpio(self,gpio,value):
        with open(self.url_base+gpio+"/value",'w+') as fd:
            fd.write(str(value))
        return value

    def read_gpio(self,gpio):
        with open(self.url_base+gpio+"/value",'r+') as fd:
            return fd.read()
            
    def config_write(self,gpio,dir=None,drive=None,value=0):
        self.config_gpio(gpio,dir,drive)
        return self.write_gpio(gpio,value)