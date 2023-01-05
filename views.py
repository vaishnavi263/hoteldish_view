from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .models import Dish

# Create your views here.
class DishesView(APIView):
    def get(self,request,*args,**kwargs):
        all_dishes=Dish.objects.all()
        serializer=self.serializer_class(all_dishes,many=True)
        return Response(data=serializer.data)

    def post(self,request,*args,**kwargs) :
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)       

class Dishdetailsview(APIView):
    serializer_class=Dishesmodelserializer
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        try:
            dish_detail=Dish.objects.get(id=id)
            serializer=self.serializer_class(dish_detail)
            return Response(data=serializer.data)
        except:
            return Response({'msg':"invalid"})  

    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        try:
            dish_detail=Dish.objects.get(id=id)
            dish_detail.delete()
            serializer=self.serializer_class(dish_detail)
            return Response(data=serializer.data)
        except:
            return Response({'msg':"invaid"})              

class Dishmodelviewset(ModelViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=Dishesmodelserializer 
    queryset=Dish.objects.all()
    model=Dish       