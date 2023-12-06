from django.http import HttpResponse

class SampleMiddleware(object):
	def __inti__(self,get_response):
		self.get_response=get_response
	def __call__(self,request):
		response=self.get_response(request)
		return response
		def process_exception(self,request,exception):
			return HttpResponse('<h1>Currently We Are Facing Technical Issue ,Please visit After some time..!!!!</h1')