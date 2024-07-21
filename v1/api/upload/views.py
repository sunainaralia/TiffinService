from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, JSONParser

import cloudinary.uploader
import cloudinary.api


class UploadView(APIView):
    parser_classes = (
        MultiPartParser,
        JSONParser,
    )

    @staticmethod
    def post(request):
        try:
            file = request.data.get("image")

            if not file:
                return Response(
                    {"msg": "No file provided"},
                    status=400,
                )
            upload_data = cloudinary.uploader.upload(file, folder="TiffinService")

            return Response(
                {
                    "msg": "image saved successfully",
                    "ImageUrl": upload_data["url"],
                },
                status=201,
            )
        except cloudinary.exceptions.Error as e:
            return Response(
                {"status": "failed", "message": str(e)},
                status=500,
            )
        except Exception as e:
            return Response(
                {
                    "status": "failed",
                    "message": "An error occurred while uploading the image",
                },
                status=500,
            )
