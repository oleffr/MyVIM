#ifndef _MY_STRING_
#define _MY_STRING_

#include <iostream>


class MyString {
    private:
        char* _ptr;
        size_t _size;
        size_t _capacity;
        
public:
    //CONSTRUCTORS
        MyString(void);
        MyString(char* data_str);
        MyString(const std::initializer_list<char>& array);
        MyString(std::string& data_str);
        MyString(char* data_str, const size_t count);
        MyString(const size_t count, char symbol);
        MyString(MyString& another);
        ~MyString();

    //GETTERS
        char* c_str() const;
        void clear();
        char* data() const;
        bool empty() const;
        size_t length() const;
        size_t capacity() const;
        size_t size() const;
        void shrink_to_fit();
    
    //OPERATORS
        MyString & operator+(MyString& another);
        MyString & operator+(const char* cur_string);
        MyString & operator+(const std::string& data_str);
        MyString & operator+=(char* data_str);
        MyString & operator+=(const std::string& data_str);
        MyString & operator+=(MyString& another);
        MyString & operator=(char* data_str);
        MyString & operator=(std::string& сur_str);
        MyString & operator=(char symbol);
        MyString & operator=(MyString & another);
        char & operator[](const size_t index);

        bool operator>(const MyString& another);
        bool operator>(char* data_str);
        bool operator<(const MyString& another);
        bool operator<(char* data_str);
        bool operator>=(const MyString& another);
        bool operator>=(char* data_str);
        bool operator<=(const MyString& another);
        bool operator<=(char* data_str);
        bool operator!=(const MyString& another);
        bool operator!=(char* data_str);
        bool operator ==(const MyString& another);
        bool operator ==(char* data_str);
        bool operator ==(char data_str);
        friend std::ostream& operator<<(std::ostream& out, MyString& another);
        friend std::istream& operator>>(std::istream& in, MyString& another);

    //FUNCTIONS
        void insert(const size_t index, const size_t count, const char symbol);
        void insert(const size_t index, const char* string);
        void insert(const size_t index, const char* string, const size_t count);
        void insert(const size_t index, std::string& data_str);
        void insert(const size_t index, std::string& data_str, const size_t count);

        void erase(const size_t index, const size_t count);

        void append(const size_t count, const char symbol);
        void append(const char* data_str);
        void append(const char* data_str, const size_t index, const size_t count);
        void append(std::string& data_str);
        void append(std::string& data_str, const size_t index, const size_t count);

        void replace(const size_t index, const size_t count, const char* data_str);
        void replace(const size_t index, const size_t count, std::string& data_str);

        size_t find(const char* data_str);
        size_t find(const char* data_str, const size_t index);
        size_t find(std::string& data_str);
        size_t find(std::string& data_str, const size_t index);

        MyString & substr(const size_t index);
        MyString & substr(const size_t index, const size_t count);
};

#endif