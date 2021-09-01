# credits: https://github.com/atlasfoo

class ReadWriteSerializerMixin(object):
    """
    Overrides get_serializer_class to choose the read serializer
    for GET requests and the write serializer for POST requests.
    Set read_serializer_class and write_serializer_class attributes on a
    viewset.
    """

    read_serializer_class = None
    write_serializer_class = None

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return self.get_write_serializer_class()
        return self.get_read_serializer_class()

    def get_read_serializer_class(self):
        assert self.read_serializer_class is not None, (
                "'%s' should either include a `read_serializer_class` attribute,"
                "or override the `get_read_serializer_class()` method."
                % self.__class__.__name__
        )
        return self.read_serializer_class

    def get_write_serializer_class(self):
        assert self.write_serializer_class is not None, (
                "'%s' should either include a `write_serializer_class` attribute,"
                "or override the `get_write_serializer_class()` method."
                % self.__class__.__name__
        )
        return self.write_serializer_class


class MultiSerializerMixin(object):
    """
    Defines a different serializer for each method of a viewset.
    Implement read_serializer_class, create_serializer_class, update_serializer_class,
    partial_update_serializer_class and destroy_serializer_class if methods implemented.
    """

    read_serializer_class = None
    create_serializer_class = None
    update_serializer_class = None
    partial_update_serializer_class = None
    destroy_serializer_class = None

    def get_serializer_class(self):
        if self.action == "create":
            return self.get_create_serializer_class()
        elif self.action == "update":
            return self.get_update_serializer_class()
        elif self.action == "partial_update":
            return self.get_partial_update_serializer_class()
        elif self.action == "destroy":
            return self.get_destroy_serializer_class()

        return self.get_read_serializer_class()

    def get_read_serializer_class(self):
        assert self.read_serializer_class is not None, (
                "'%s' should either include a `read_serializer_class` attribute,"
                "or override the `get_read_serializer_class()` method."
                % self.__class__.__name__
        )
        return self.read_serializer_class

    def get_create_serializer_class(self):
        assert self.create_serializer_class is not None, (
                "'%s' should either include a `create_serializer_class` attribute,"
                "or override the `get_create_serializer_class()` method."
                % self.__class__.__name__
        )
        return self.create_serializer_class

    def get_update_serializer_class(self):
        assert self.update_serializer_class is not None, (
                "'%s' should either include a `update_serializer_class` attribute,"
                "or override the `get_update_serializer_class()` method."
                % self.__class__.__name__
        )
        return self.update_serializer_class

    def get_partial_update_serializer_class(self):
        assert self.partial_update_serializer_class is not None, (
                "'%s' should either include a `partial_update_serializer_class` attribute,"
                "or override the `get_partial_update_serializer_class()` method."
                % self.__class__.__name__
        )
        return self.partial_update_serializer_class

    def get_destroy_serializer_class(self):
        assert self.destroy_serializer_class is not None, (
                "'%s' should either include a `destroy_serializer_class` attribute,"
                "or override the `get_destroy_serializer_class()` method."
                % self.__class__.__name__
        )
        return self.destroy_serializer_class