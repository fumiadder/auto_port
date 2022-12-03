class BootStrapModelForm(object):
    bootstrap_exclude_list = []  # 自定制排除bootstrap样式列表

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name in self.bootstrap_exclude_list:
                continue
            old_class = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = '{} form-control'.format(old_class)
            field.widget.attrs['placeholder'] = f'请输入{field.label}'
