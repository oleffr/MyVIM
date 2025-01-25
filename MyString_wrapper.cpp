#include <pybind11/pybind11.h>
#include "MyString.h"

namespace py = pybind11;

PYBIND11_MODULE(MyString, m) {
    py::class_<MyString>(m, "MyString")
        //CONSTRUCTORS
        .def(py::init<>())
        .def(py::init<char*>())
        .def(py::init<const std::initializer_list<char>&>())
        .def(py::init<std::string& >())
        
        .def(py::init<char*, const size_t>())
        .def(py::init<const size_t, char>())
        .def(py::init<MyString&>())

        //GETTERS
        .def("size", static_cast<size_t (MyString::*)() const>(&MyString::size))
        .def("capacity", static_cast<size_t (MyString::*)() const>(&MyString::capacity))
        .def("length", static_cast<size_t (MyString::*)() const>(&MyString::length))
        .def("c_str", static_cast<char* (MyString::*)() const>(&MyString::c_str))
        .def("data", static_cast<char* (MyString::*)() const>(&MyString::data))
        .def("empty", static_cast<bool (MyString::*)() const>(&MyString::empty))

        //FUNCTIONS
        .def("shrink_to_fit", static_cast<void (MyString::*)()>(&MyString::shrink_to_fit))
        .def("clear", static_cast<void (MyString::*)()>(&MyString::clear))
        .def("erase", static_cast<void (MyString::*)(const size_t, const size_t)>(&MyString::erase))

        //INSERT
        .def("insert", static_cast<void (MyString::*)(const size_t, const size_t, const char)>(&MyString::insert))
        .def("insert", static_cast<void (MyString::*)(const size_t,const char*)>(&MyString::insert))
        .def("insert", static_cast<void (MyString::*)(const size_t, const char*, const size_t)>(&MyString::insert))
        .def("insert", static_cast<void (MyString::*)(const size_t, std::string&)>(&MyString::insert))
        .def("insert", static_cast<void (MyString::*)(const size_t, std::string&, const size_t)>(&MyString::insert))

        //APPEND
        .def("append", static_cast<void (MyString::*)(const size_t, const char)>(&MyString::append))
        .def("append", static_cast<void (MyString::*)(const char*)>(&MyString::append))
        .def("append", static_cast<void (MyString::*)(const char*, const size_t, const size_t)>(&MyString::append))
        .def("append", static_cast<void (MyString::*)(std::string&)>(&MyString::append))
        .def("append", static_cast<void (MyString::*)(std::string&, const size_t, const size_t)>(&MyString::append))

        //REPLACE
        .def("replace", static_cast<void (MyString::*)(const size_t, const size_t, const char*)>(&MyString::replace))
        .def("replace", static_cast<void (MyString::*)(const size_t, const size_t, std::string&)>(&MyString::replace))

        //SUBSTR
        .def("substr", static_cast<MyString & (MyString::*)(const size_t)>(&MyString::substr), pybind11::return_value_policy::reference)
        .def("substr", static_cast<MyString & (MyString::*)(const size_t, const size_t)>(&MyString::substr), pybind11::return_value_policy::reference)

        //FIND
        .def("find", static_cast<size_t (MyString::*)(const char*)>(&MyString::find))
        .def("find", static_cast<size_t (MyString::*)(const char*, const size_t)>(&MyString::find))
        .def("find", static_cast<size_t (MyString::*)(std::string&)>(&MyString::find))
        .def("find", static_cast<size_t (MyString::*)(std::string&, const size_t)>(&MyString::find))

        //OPERATORS - add
        .def("__add__", static_cast<MyString & (MyString::*)(MyString&)>(&MyString::operator+), pybind11::return_value_policy::reference)
        .def("__add__", static_cast<MyString & (MyString::*)(const char*)>(&MyString::operator+), pybind11::return_value_policy::reference)
        .def("__add__", static_cast<MyString & (MyString::*)(const std::string&)>(&MyString::operator+), pybind11::return_value_policy::reference)

        //OPERATORS - assign
        .def("__assign__", static_cast<MyString & (MyString::*)(MyString&)>(&MyString::operator=), pybind11::return_value_policy::reference)
        .def("__assign__", static_cast<MyString & (MyString::*)(char*)>(&MyString::operator=), pybind11::return_value_policy::reference)
        .def("__assign__", static_cast<MyString & (MyString::*)(std::string&)>(&MyString::operator=), pybind11::return_value_policy::reference)
        .def("__assign__", static_cast<MyString & (MyString::*)(char)>(&MyString::operator=), pybind11::return_value_policy::reference)

        //OPERATORS - more
        .def("__gt__", static_cast<bool (MyString::*)(const MyString&)>(&MyString::operator>))
        .def("__gt__", static_cast<bool (MyString::*)(char*)>(&MyString::operator>))

        //OPERATORS - moreeq
        .def("__ge__", static_cast<bool (MyString::*)(const MyString&)>(&MyString::operator>=))
        .def("__ge__", static_cast<bool (MyString::*)(char*)>(&MyString::operator>=))

        //OPERATORS - less
        .def("__lt__", static_cast<bool (MyString::*)(const MyString&)>(&MyString::operator<))
        .def("__lt__", static_cast<bool (MyString::*)(char*)>(&MyString::operator<))

        //OPERATORS - lesseq
        .def("__le__", static_cast<bool (MyString::*)(const MyString&)>(&MyString::operator<=))
        .def("__le__", static_cast<bool (MyString::*)(char*)>(&MyString::operator<=))

        // //OPERATORS - equal
        .def("__eq__", static_cast<bool (MyString::*)(const MyString&)>(&MyString::operator==))
        .def("__eq__", static_cast<bool (MyString::*)(char*)>(&MyString::operator==))

        //OPERATORS - equal
        .def("__ne__", static_cast<bool (MyString::*)(const MyString&)>(&MyString::operator!=))
        .def("__ne__", static_cast<bool (MyString::*)(char*)>(&MyString::operator!=))

        //OPERATORS - addassign
        .def("__iadd__", (MyString & (MyString::*)(const std::string&)) & MyString::operator+=)
        .def("__iadd__", (MyString & (MyString::*)(char*)) & MyString::operator+=)
        .def("__iadd__", static_cast<MyString & (MyString::*)(MyString&)>(&MyString::operator+=), pybind11::return_value_policy::reference)
        ;

}
