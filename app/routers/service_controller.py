from fastapi import APIRouter, Depends
from utils.jwt_verify import get_current_active_user
from utils.verify_model import DirectoryInput, User
from models.file_system_model import FileSystemModel
from models.service_model import ServiceModel


service_router = APIRouter()


@service_router.post("/service/list_dir", tags=["Service"])
# def service_list_dir(path_input: DirectoryInput):
def service_list_dir(path_input: DirectoryInput, current_user: User = Depends(get_current_active_user)):
    available_path = FileSystemModel().list_dir(path_input.path)
    service_model = ServiceModel()
    object = service_model.get_object_id(path_input.path)
    if object is None:
        return []
    user_privileges = service_model.get_privileges(object.object_id, 1)
    project_privileges = service_model.get_privileges(object.object_id, 2)
    for object in project_privileges:
        if object not in user_privileges:
            user_privileges.append(object)
    result = []
    for path in user_privileges:
        result.append(available_path[path['object_name']])
    return result
