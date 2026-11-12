def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    for field_name in ["password1", "password2"]:
        self.fields[field_name].widget.attrs.update({
            "class": "w-full block bg-transparent outline-none text-base py-1",
            "placeholder": "Enter your password",
        })
