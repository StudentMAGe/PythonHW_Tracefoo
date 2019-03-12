import sys


def tracefoo(userfunc):
    global nameofuserfunc
    nameofuserfunc = userfunc.__name__
    sys.settrace(tracefunc)


def tracefunc(frame, event, arg):
    if event == "return" and frame.f_code.co_name == nameofuserfunc:
        print(event, "function:", frame.f_code.co_name, ", local vars:", list(frame.f_locals.keys()),
              ", globals:", frame.f_globals)
        return tracefunc

