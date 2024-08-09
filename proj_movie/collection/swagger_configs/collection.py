from drf_yasg import openapi

COLLECTION_CREATION_UPDATED_SCHEMA = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "title": openapi.Schema(
            type=openapi.TYPE_STRING,
            description="Title of the Collection"
        ),
        "description": openapi.Schema(
            type=openapi.TYPE_STRING,
            description="This parameter takes description for the Collection"
        ),
        "movies": openapi.Schema(
            type=openapi.TYPE_ARRAY,
            description="This parameter takes a list of movie object",
            items=openapi.Items(
                type=openapi.TYPE_OBJECT,
                properties={
                    "uuid": openapi.Schema(
                        type=openapi.FORMAT_UUID,
                        description="UUid of the movie object"
                    ),
                    "title": openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description="Title of the Movie"
                    ),
                    "description": openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description="This parameter takes description for the movie"
                    ),
                    "genres": openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description="This parameter takes genres for the movie"
                    )
                }
            ),
        ),
    }
)

PATH_COLLECTION_ID = openapi.Parameter(
    name="collection_uuid",
    type=openapi.TYPE_STRING,
    in_=openapi.IN_PATH,
    description="UUId of the collection that needs to be updated"
)
