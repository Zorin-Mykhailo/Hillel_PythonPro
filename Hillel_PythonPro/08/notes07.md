- [Dunder methods | Pydon't 🐍](https://mathspp.com/blog/pydonts/dunder-methods) @mathspp.com


| Dunder method |	Usage / Needed for | Link |
| --- | --- | --- |
| \_\_init\_\_ | Initialise object ||
| \_\_new\_\_ | Create object ||
| \_\_del\_\_ | Destroy object ||
| \_\_repr\_\_ | Compute “official” string representation / repr(obj) ||
| \_\_str\_\_ | Pretty print object / str(obj) / print(obj) ||
| __bytes__ | bytes(obj) ||
| \_\_format\_\_ | Custom string formatting ||
| \_\_lt\_\_ | obj < ... ||
| \_\_le\_\_ | obj <= ... ||
| \_\_eq\_\_ | obj == ... ||
| \_\_ne\_\_ | obj != ... ||
| \_\_gt\_\_ | obj > ... ||
| \_\_ge\_\_ | obj >= ... ||
| \_\_hash\_\_ | hash(obj) / object as dictionary key ||
| \_\_bool\_\_ | bool(obj) / define Truthy/Falsy value of object ||
| \_\_getattr\_\_ | Fallback for attribute access ||
| \_\_getattribute\_\_ | Implement attribute access: obj.name ||
| \_\_setattr\_\_ | Set attribute values: obj.name = value ||
| \_\_delattr\_\_ | Delete attribute: del obj.name ||
| \_\_dir\_\_ | dir(obj) ||
| \_\_get\_\_ | Attribute access in descriptor ||
| \_\_set\_\_ | Set attribute in descriptor ||
| \_\_delete\_\_ | Attribute deletion in descriptor ||
| \_\_init_subclass\_\_ | Initialise subclass ||
| \_\_set_name\_\_ | Owner class assignment callback ||
| \_\_instancecheck\_\_ | isinstance(obj, ...) ||
| \_\_subclasscheck\_\_ | issubclass(obj, ...) ||
| \_\_class_getitem\_\_ | Emulate generic types ||
| \_\_call\_\_ | Emulate callables / obj(*args, **kwargs) ||
| \_\_len\_\_ | len(obj) ||
| \_\_length_hint\_\_ | Estimate length for optimisation purposes ||
| \_\_getitem\_\_ | Access obj[key] ||
| \_\_setitem\_\_ | obj[key] = ... or `obj[] ||
| \_\_delitem\_\_ | del obj[key] ||
| \_\_missing\_\_ | Handle missing keys in dict subclasses ||
| \_\_iter\_\_ | iter(obj) / for ... in obj (iterating over) ||
| \_\_reversed\_\_ | reverse(obj) ||
| \_\_contains\_\_ | ... in obj (membership test) ||
| \_\_add\_\_ | obj + ... ||
| \_\_radd\_\_ | ... + obj ||
| \_\_iadd\_\_ | obj += ... ||
| \_\_sub\_\_ 2 3 | obj - ... ||
| \_\_mul\_\_ 2 3 | obj * ... ||
| \_\_matmul\_\_ 2 3 | obj @ ... ||
| \_\_truediv\_\_ 2 3 | obj / ... ||
| \_\_floordiv\_\_ 2 3 | obj // ... ||
| \_\_mod\_\_ 2 3 | obj % ... ||
| \_\_divmod\_\_ 2 | divmod(obj, ...) ||
| \_\_pow\_\_ 2 3 | obj ** ... ||
| \_\_lshift\_\_ 2 3 | obj << ... ||
| \_\_rshift\_\_ 2 3 | obj >> ... ||
| \_\_and\_ 2 3 | obj & ... ||
| \_\_xor\_\_ 2 3 |	obj ^ ... ||
| \_\_or\_\_ 2 3 | obj \| ... ||
| \_\_neg\_\_ | -obj (unary) ||
| \_\_pos\_\_ | +obj (unary) ||
| \_\_abs\_\_ | abs(obj) ||
| \_\_invert\_\_ | ~obj (unary) ||
| \_\_complex\_\_ | complex(obj) ||
| \_\_int\_\_ | int(obj) ||
| \_\_float\_\_ | float(obj) ||
| \_\_index\_\_ | Losslessly convert to integer ||
| \_\_round\_\_ | round(obj) ||
| \_\_trunc\_\_ | math.trunc(obj) ||
| \_\_floor\_\_ | math.floor(obj) ||
| \_\_ceil\_\_ | math.ceil(obj) ||
| \_\_enter\_\_ | with obj (enter context manager) ||
| \_\_exit\_\_ | with obj (exit context manager) ||
| \_\_await\_\_ | Implement awaitable objects ||
| \_\_aiter\_\_ | aiter(obj) ||
| \_\_anext\_\_ | anext(obj) ||
| \_\_aenter\_\_ | async with obj (enter async context manager) ||
| \_\_aexit\_\_ | async with obj (exit async context manager) ||
