import os

class Helper(object):
	@staticmethod
	def flat_dict(d, delimiter="/", start_char="^", end_char="$", key="", out={}):
		for k,v in d.iteritems():
			new_key = key + delimiter + k
			if isinstance(v, dict):
				Helper.flat_dict(v, delimiter, start_char, end_char, new_key, out)
			else:
				out[start_char + new_key + end_char] = v
		return out
		
class Singleton(type):
     def __init__(cls, name, bases, dict):
         super(Singleton, cls).__init__(name, bases, dict)
         cls.instance = None
         
     def __call__(cls,*args,**kw):
         if cls.instance is None:
             cls.instance = super(Singleton, cls).__call__(*args, **kw)
         return cls.instance
         
class Importer(object):
	@staticmethod
	def import_class(cl):
		d = cl.rfind(".")
		classname = cl[d+1:len(cl)]
		m = __import__(cl[0:d], globals(), locals(), [classname])
		return getattr(m, classname)
		
	@staticmethod
	def import_module(module):
		d = module.rfind(".")
		modulename = module[d+1:len(module)]
		mod = __import__(module, globals(), locals(), [modulename])
		return mod
		
	@staticmethod
	def module_path(module):
		result = os.path.dirname(Importer.import_module(module).__file__)
		return result
