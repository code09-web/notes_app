from rest_framework.response import Response
from rest_framework import status 
from rest_framework import permissions
from .models import NotesModel
from .serializers import NoteSerializers,NoteSerializersForPut
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
class NotesView(GenericAPIView):
    
    # 1. list all
    parser_classes = [MultiPartParser,FormParser,JSONParser]
    serializer_class=NoteSerializers
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request,*args,**kwargs):
        notes=NotesModel.objects.filter(user=request.user.id)
        serializer=NoteSerializers(notes,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    # 2. Create
    def post(self,request,*args,**kwargs):
        
        data={
            'title':request.data.get('title'),
            'body':request.data.get('body'),
            'user':request.user.id,
            'image':request.data.get('image')
        }
        serializer=NoteSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

    



class NotesDetailView(GenericAPIView):
    serializer_class=NoteSerializersForPut
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    parser_classes = [MultiPartParser,FormParser,JSONParser]

    def get_object(self,notes_id,user_id=None):
        '''
        Helper method to get the object with given todo_id, and user_id
        '''
        try:
            if user_id is None:
                return NotesModel.objects.get(id=notes_id)
            else:
                return NotesModel.objects.get(id=notes_id,user=user_id)


        except NotesModel.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self,request,notes_id,*args, **kwargs):
        
        # Retrieves the todo with given todo_id
        print(request.user.id)
        if request.user.id==None:
            notes_instance=self.get_object(notes_id)
        else:
            notes_instance=self.get_object(notes_id,request.user.id)
        if not notes_instance:
            return Response(
                {"res": "Object with notes id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer=NoteSerializers(notes_instance)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    # 4. Update
    def put(self,request,notes_id ,*args,**kwargs):
        notes_instance=self.get_object(notes_id,request.user.id)
        if not notes_instance:
            return Response(
                {"res":"Object with notes id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data={
            'title':request.data.get('title'),
            'body':request.data.get('body'),
            'user':request.user.id,
            'image':request.data.get('image')
        }
        serializer=NoteSerializersForPut(instance=notes_instance,data=data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data,"message":"updated successfully "},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
        # 5. Delete
    def delete(self, request, notes_id, *args, **kwargs):
        '''
        Deletes the todo item with given todo_id if exists
        '''
        todo_instance = self.get_object(notes_id, request.user.id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        todo_instance.delete()
        return Response(
            {"res": "Note has been deleted!"},
            status=status.HTTP_200_OK
        )

