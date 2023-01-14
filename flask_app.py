import random
import time
import flask
import os
import imp
import Files_check as sol
import Files_check.exc1_sol , Files_check.exc2_sol , Files_check.exc3_sol ,Files_check.exc4_sol , Files_check.exc5_sol

app = flask(__name__)

@app.route('/')
def main():
    return flask.send_from_directory("", "Entrance_page.html")

@app.route('/try')
def maing():
    return flask.send_from_directory("", "try.html")

@app.route('/exc1')
def Enter_sol_exc1():
    return flask.send_from_directory("Exercise/exc", "exc1.html")

@app.route("/exc1_check_sol", methods=["POST"])
def Check_sol_exc1():
    try:
        fname = f"file_{round(time.time())}.py"
        with open(fname, 'w') as fh:
            fh.write(flask.request.form['w3review'])
        # load the new module
        fname = fname.split(".")[0]
        fp, pathname, description = imp.find_module(f"{fname}")
        file = imp.load_module("test_module", fp, pathname, description)
        func = file.sol
        for i in range(100):
            x = func(i)
            if x != Files_check.exc1_sol.exc1_sol(i):
                os.remove(fname + ".py")
                return flask.send_from_directory("Exercise/exc_false", "exc1_false.html")
        os.remove(fname + ".py")
        return flask.send_from_directory("Exercise/exc_true", "exc1_true.html")
    except:
        os.remove(fname + ".py")
        return flask.send_from_directory("Exercise/exc_false", "exc1_false.html")



@app.route('/exc2')
def Enter_sol_exc2():
    return flask.send_from_directory("Exercise/exc", "exc2.html")

@app.route("/exc2_check_sol", methods=["POST"])
def Check_sol_exc2():
    try:
        fname = f"file_{round(time.time())}.py"
        with open(fname, 'w') as fh:
            fh.write(flask.request.form['w3review'])
        # load the new module
        fname = fname.split(".")[0]
        fp, pathname, description = imp.find_module(f"{fname}")
        file = imp.load_module("test_module", fp, pathname, description)
        func = file.sol

        for i in range(10,100):
            x = func(i)
            if x != Files_check.exc2_sol.exc2_sol(i):
                os.remove(fname + ".py")
                return flask.send_from_directory("Exercise/exc_false", "exc2_false.html")
        os.remove(fname + ".py")
        return flask.send_from_directory("Exercise/exc_true", "exc2_true.html")
    except:
        os.remove(fname + ".py")
        return flask.send_from_directory("Exercise/exc_false", "exc2_false.html")



@app.route('/exc3')
def Enter_sol_exc3():
    return flask.send_from_directory("Exercise/exc", "exc3.html")

@app.route("/exc3_check_sol", methods=["POST"])
def Check_sol_exc3():
    try:
        fname = f"file_{round(time.time())}.py"
        with open(fname, 'w') as fh:
            fh.write(flask.request.form['w3review'])

        # load the new module
        fname = fname.split(".")[0]
        fp, pathname, description = imp.find_module(f"{fname}")
        file = imp.load_module("test_module", fp, pathname, description)
        func = file.sol
        a=""
        for i in range(100):
            import string
            string.ascii_letters
            a=a+random.choice(string.ascii_letters)
            x = func(a)
            if x != Files_check.exc3_sol.exc3_sol(a):
                os.remove(fname + ".py")
                return flask.send_from_directory("Exercise/exc_false", "exc3_false.html")
        os.remove(fname + ".py")
        return flask.send_from_directory("Exercise/exc_true", "exc3_true.html")
    except:
        os.remove(fname + ".py")
        return flask.send_from_directory("Exercise/exc_false", "exc3_false.html")


@app.route('/exc4')
def Enter_sol_exc4():
    return flask.send_from_directory("Exercise/exc", "exc4.html")

@app.route("/exc4_check_sol", methods=["POST"])
def Check_sol_exc4():
    print("f")
    try:
        fname = f"file_{round(time.time())}.py"
        with open(fname, 'w') as fh:
            fh.write(flask.request.form['w3review'])

        # load the new module
        fname = fname.split(".")[0]
        fp, pathname, description = imp.find_module(f"{fname}")
        file = imp.load_module("test_module", fp, pathname, description)
        func = file.sol
        a=""
        for i in range(100):
            import string
            string.ascii_letters
            a=a+random.choice(string.ascii_letters)
            x = func(a)
            if x != Files_check.exc4_sol.exc4_sol(a):
                os.remove(fname + ".py")
                return flask.send_from_directory("Exercise/exc_false", "exc4_false.html")
        os.remove(fname + ".py")
        return flask.send_from_directory("Exercise/exc_true", "exc4_true.html")
    except:
        os.remove(fname + ".py")
        return flask.send_from_directory("Exercise/exc_false", "exc4_false.html")


@app.route('/exc5')
def Enter_sol_exc5():
    return flask.send_from_directory("Exercise/exc", "exc5.html")

@app.route("/exc5_check_sol", methods=["POST"])
def Check_sol_exc5():
    try:
        fname = f"file_{round(time.time())}.py"
        with open(fname, 'w') as fh:
            fh.write(flask.request.form['w3review'])

        # load the new module
        fname = fname.split(".")[0]
        fp, pathname, description = imp.find_module(f"{fname}")
        file = imp.load_module("test_module", fp, pathname, description)
        func = file.sol
        a=""
        for i in range(100):
            import string
            string.ascii_letters
            a=a+random.choice(string.ascii_letters)
            x = func(a , i%24)
            if x != Files_check.exc5_sol.exc5_sol(a , i%24):
                os.remove(fname + ".py")
                return flask.send_from_directory("Exercise/exc_false", "exc5_false.html")
        os.remove(fname + ".py")
        return flask.send_from_directory("Exercise/exc_true", "exc5_true.html")
    except:
        os.remove(fname + ".py")
        return flask.send_from_directory("Exercise/exc_false", "exc5_false.html")


