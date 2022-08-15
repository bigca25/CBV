# from django.shortcuts import render,HttpResponse
# from django.views import View
# from rest_framework.views import APIView
# Create your views here.
# class BookView(View):
#
# 	def dispatch(self, request, *args, **kwargs):
# 		print('hello world')
# 		ret = super().dispatch(request, *args, **kwargs)
# 		return ret
#
# 	def get(self,request):
# 		print('get方法已经执行')
# 		return HttpResponse('View GET请求。。。')
#
# 	def post(self,request):
# 		return HttpResponse('View POST请求。。。')
#
# 	def delete(self, request):
# 			return HttpResponse('View DELETE请求。。。')

from django.shortcuts import render,HttpResponse

from rest_framework.views import APIView

class BookView(APIView):
	def get(self, request):
		print ('get方法已经执行')
		return HttpResponse('APIView GET请求。。。')

	def post(self, request):
		return HttpResponse('APIView POST请求。。。')

	def delete(self, request):
		return HttpResponse('APIView DELETE请求。。。')