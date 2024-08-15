from flask import request, jsonify
from flask.views import MethodView


class BaseView(MethodView):
    permission_classes = []

    def dispatch_request(self, **kwargs):
        if not self.check_permissions():
            return jsonify({'error': 'Unauthorized'}), 403
        return super().dispatch_request(**kwargs)

    def check_permissions(self):
        for permission in self.permission_classes:
            if not permission().has_permission(request):
                return False
        return True

    def get(self, *args, **kwargs):
        if kwargs:
            return self.get_detail(*args, **kwargs)
        else:
            return self.get_list(*args, **kwargs)

    def post(self, *args, **kwargs):
        return self.create(*args, **kwargs)

    def put(self, *args, **kwargs):
        return self.update(*args, **kwargs)

    def delete(self, *args, **kwargs):
        return self.destroy(*args, ** kwargs)

    def get_list(self, *args, **kwargs):
        raise NotImplementedError("Implement get_list method")

    def get_detail(self, *args, **kwargs):
        raise NotImplementedError("Implement get_detail method")

    def create(self, *args, **kwargs):
        raise NotImplementedError("Implement create method")

    def update(self, *args, **kwargs):
        raise NotImplementedError("Implement update method")

    def destroy(self, *args, **kwargs):
        raise NotImplementedError("Implement delete_item method")
