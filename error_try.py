def trying():

    try:
        f = open('testfile','r') #mettre w pour que ça marche
        f.write('Write a test line')
    except TypeError:
        print('The is a type error')
    except OSError:
        print('there is a OS error !')
    finally:
        print('I always run')


print(hello())
