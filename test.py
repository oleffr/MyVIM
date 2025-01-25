from MyTextModel import MyTextModel

def test_set_cursor():
    test_mod = MyTextModel()

    #print(test_mod.return_coordinates())
    assert (test_mod.return_coordinates() == [0,1]), print("error in base coordinates")

    test_mod.set_coordinates(1,3)
    #print(test_mod.return_coordinates())
    assert (test_mod.return_coordinates() == [1,3]), print("AssertionError")

    test_mod.set_coordinates(0,3)
    #print(test_mod.return_coordinates())
    assert test_mod.return_coordinates() == [0,3], print("AssertionError")
    
    test_mod.set_coordinates(1,0)
    #print(test_mod.return_coordinates())
    assert test_mod.return_coordinates() == [1,0], print("AssertionError")

    test_mod.set_coordinates(3,0)
    #print(test_mod.return_coordinates())
    assert test_mod.return_coordinates() == [3,0], print("AssertionError")
    

def test_module_curs_move():
    test_mod = MyTextModel()

    text1 = """hello11234455677
hi
my world
lovely world
world"""

    text_arr = text1.split("\n")

    test_mod.text_arr = text_arr

    text = "world"

    test_mod.do_right()
    assert test_mod.return_coordinates() == [1,1], print("AssertionError")

    test_mod.do_left()
    test_mod.do_left()
    #print(test_mod.return_coordinates())  
    assert test_mod.return_coordinates() == [0,1], print("AssertionError")


    test_mod.do_up()
    #print(test_mod.return_coordinates())
    assert test_mod.return_coordinates() == [0,1], print("AssertionError")

    test_mod.do_down()
    #print(test_mod.return_coordinates())
    assert test_mod.return_coordinates() == [0,2], print("AssertionError")
    

def test_search():
    filename = "/Users/oleffr/Desktop/Учеба/ООП/4/1.txt"
    test_mod = MyTextModel()
    test_mod.write_in_buf(filename)

    ##
    test_mod.set_coordinates(4, 1)
    test_mod.search_right("1.txt")
    print(test_mod.return_coordinates())

    test_mod.second_search_n()
    print(test_mod.return_coordinates())

    test_mod.second_search_n()
    print(test_mod.return_coordinates())
    test_mod.second_search_n()
    print(test_mod.return_coordinates())

    test_mod.second_search_N()
    print(test_mod.return_coordinates())
    test_mod.second_search_N()
    print(test_mod.return_coordinates())
    test_mod.second_search_n()
    print(test_mod.return_coordinates())
    ##

    test_mod.set_coordinates(2,4)
    test_mod.do_command_null()
    #print(test_mod.return_coordinates())
    assert test_mod.return_coordinates() == [0,4], print("AssertionError")

    test_mod.set_coordinates(2,4)
    test_mod.do_command_endline()
    #print(test_mod.return_coordinates())
    assert test_mod.return_coordinates() == [19,4], print("AssertionError")

    test_mod.do_command_gg()
    #print(test_mod.return_coordinates())
    assert test_mod.return_coordinates() == [0,1], print("AssertionError")

    test_mod.do_command_G()
    #print(test_mod.return_coordinates())
    assert test_mod.return_coordinates() == [3,5440], print("AssertionError")

    test_mod.do_command_NG(3)
    #print(test_mod.return_coordinates())
    assert test_mod.return_coordinates() == [0,3], print("AssertionError")

    test_mod.do_command_NG(4)
    #print(test_mod.return_coordinates())
    assert test_mod.return_coordinates() == [0,4], print("AssertionError")

    test_mod.set_coordinates(0,0)
    test_mod.search_right("hello")
    #print(test_mod.return_coordinates())
    assert test_mod.return_coordinates() == [8, 1], print("AssertionError")

    test_mod.second_search_n()
    #print(test_mod.return_coordinates())
    assert test_mod.return_coordinates() == [7, 6], print("AssertionError")
   
    test_mod.set_coordinates(8,4)
    test_mod.search_left("1.txt")
    #print(test_mod.return_coordinates())
    assert test_mod.return_coordinates() == [2,1], print("AssertionError")

    test_mod.second_search_N()
    #print(test_mod.return_coordinates())
    assert test_mod.return_coordinates() == [19, 5], print("AssertionError")
    

def test_text_working():
    filename = "/Users/oleffr/Desktop/Учеба/ООП/4/2.txt"
    test_mod = MyTextModel()
    test_mod.write_in_buf(filename)

    assert test_mod.text_arr == ["hello hello1 hello\n"], print("AssertionError")

    test_mod.do_command_diw()
    print(test_mod.text_arr)
    assert test_mod.text_arr == ["hello hello1 hello hello1 hello\n"], print("AssertionError")

    test_mod.do_command_dd()   
    assert test_mod.text_arr ==  [""], print("AssertionError")

    test_mod.text_arr == ["hello hello1 hello\n"]
    test_mod.x = 1
    test_mod.y = 1
    test_mod.do_command_yy()
    assert test_mod.copy_str == "", print("AssertionError")


test_set_cursor() 
test_module_curs_move()
test_search()
test_text_working()