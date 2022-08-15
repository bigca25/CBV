from django.shortcuts import render,HttpResponse,redirect
from .models import Books
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response

# 针对模型设计序列化器
# class BookSerializers(serializers.Serializer):
# 	title = serializers.CharField(max_length = 32)
# 	price = serializers.IntegerField() # required = False
# 	date = serializers.DateField(source = 'pub_date' )
#
# 	def create(self, validated_data):
# 		new_book = Books.objects.create (**self.validated_data)
# 		return new_book
#
# 	def update(self, instance, validated_data):
# 		Books.objects.filter (pk = instance.pk).update (**validated_data)
# 		updated_book = Books.objects.get (pk = instance.pk)
# 		return updated_book

class BookSerializers(serializers.ModelSerializer):
	date = serializers.DateField(source = "pub_date")
	class Meta:
		model = Books
		# fields = "__all__"
		# fields = ["title","price","date"]


class BookView(APIView):
	def get(self,requset):
		# 获取所有的书籍
		book_list = Books.objects.all()
		#构建序列化器对象
		serializer = BookSerializers(instance = book_list,many = True)
		return Response(serializer.data)

	def post(self,request):
		# 获取请求数据
		print('data',request.data)

		#构建序列化对象
		serializer = BookSerializers(data = request.data)
		#校验数据
		if serializer.is_valid(): #serializer.validated_data serializer.errors
			#校验通过,将数据库插入到数据库中
			# new_book = Books.objects.create(**serializer.validated_data)
			# return Response(serializer.data)
			serializer.save()
			return Response (serializer.data)

		else:
			return Response(serializer.errors)



class BookDetailView(APIView):

	def get(self,requset,id):
		book = Books.objects.get(pk=id)
		serializer = BookSerializers(instance = book, many = False)
		return Response(serializer.data)

	def put(self,request,id):
		# 获取提交的更新数据
		print("data",request.data)
		update_book = Books.objects.get (pk = id)
		# 构建序列化器对象
		serializer = BookSerializers(instance = update_book, data = request.data)
		if serializer.is_valid():
			# 更新逻辑
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors)


	def delete(self,requset,id):
		Books.objects.get(pk=id).delete()
		return Response()













