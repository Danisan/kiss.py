import os
from jinja2 import Environment, PackageLoader
from kiss.core.helpers import DictHelper, Singleton
import re
from kiss.controllers.core import Controller


class Router(object):
	__metaclass__ = Singleton
	
	def __init__(self, options):
		self.options = options
		urls = DictHelper.flat_dict(self.options["urls"])
		for k, v in urls.iteritems():
			if issubclass(v, Controller):
				urls[k] = v()
		self.options["urls"] = urls
		self.options["views"]["templates_path"] = Environment(loader=PackageLoader(self.options["views"]["templates_path"], ""))
		
	def route(self, request):
		for re_url, controller in self.options["urls"].iteritems():
			path = request.path.lower()
			match = re.match(re_url, request.path)
			if match:
				print request.path
				request.params = match.groupdict()
				action = getattr(controller, request.method.lower())
				response = action(request)
				return response
		
