#include "MyString.h"
#include <cstring>

using namespace std;

MyString::MyString() : MyString({'\0'})
{   
    // default .ctor

    this->_size = 1;
    this->_capacity = 1;
}

MyString::MyString(const std::initializer_list<char>& array) 
{ 
    // array .ctor

    this->_size = array.size()+1;
    this->_ptr = new char[this->_size+1];
    copy(begin(array), end(array), this->_ptr);
    this->_capacity = length()+1;
}

MyString::MyString(char* data_str)
{
    // char[] .ctor

    this->_size = strlen(data_str)+1;
    this->_ptr = new char[this->_size+1];
    strncpy(this->_ptr, data_str, this->_size);
    this->_capacity = length()+1;
}

MyString::MyString(std::string& data_str)
{ 
    // string .ctor

    const char* data_str1 = data_str.c_str();
    this->_size = strlen(data_str1) + 1;
    this->_ptr = new char[this->_size+1];
    strncpy(this->_ptr, data_str1, this->_size);
    this->_capacity = length() + 1;
}

MyString::MyString(const size_t count, char symbol)
{
    //const size_t count, char symbol .ctor

    this->_ptr = new char[count+1];
    this->_ptr[0] = symbol;
    this->_ptr[1] = '\0';
    this->insert(0, count-1, symbol);
    this->_ptr[count+1] = '\0';
    this->_size = count;
    this->_capacity = count+1;
}

MyString::MyString(char* data_str, const size_t count) : MyString(data_str)
{   
    // char* data_str, const size_t count .ctor

    this->erase(count, this->_size-1-count);
    this->shrink_to_fit();
}

MyString::MyString(MyString& another)
{
    // copy .ctor

    this->_size = another.size();
    this->_ptr = new char[this->_size +1];
    strncpy(this->_ptr, another.data(), this->_size+1);
    this->_capacity = length() + 1;
}

MyString::~MyString()
{
    // default destructor

    if(this->_ptr){delete this->_ptr;}
}

MyString & MyString::operator+(const std::string& data_str)
{ 
    // std::string& data_str __add__ operator

    MyString a(this->_ptr);
    MyString tmp = a + &data_str[0];
    return *this;
}

MyString & MyString::operator+(const char* data_str)
{ 
    // const char* data_str __add__ operator

    MyString tmp(this->_ptr);
    tmp.insert(strlen(this->_ptr), data_str);
    return *this;
}

MyString & MyString::operator+(MyString& another)
{
    //MyString& another __add__ operator

    insert(strlen(this->_ptr), another.data());
    MyString tmp(this->_ptr);
    return *this;
}

MyString & MyString::operator+=(char* data_str)
{ 
    // char* data_str __iadd__ operator

    this->insert(strlen(this->_ptr), data_str);
    return *this;
}
MyString & MyString::operator+=(const std::string& data_str)
{ 
    // std::string& data_str __iadd__ operator

    this->insert(strlen(this->_ptr), &data_str[0]);
    return *this;
}
MyString & MyString::operator+=(MyString& another)
{ 
    // MyString& another __iadd__ operator

    this->insert(strlen(this->_ptr), another.data());
    return *this;
}

MyString & MyString::operator=(char* data_str)
{ 
    // char* data_str __assign__ operator

    int cap = this->_capacity;
    delete this->_ptr;
    this->_ptr = new char[strlen(data_str)+1];
    this->_size = strlen(data_str)+1;
    strncpy(this->_ptr, data_str, this->_size);
    if(strlen(data_str) >= this->_capacity) { this->_capacity = length();}
    else{this->_capacity = cap;}
    return *this;
}

MyString & MyString::operator=(std::string& data_str)
{ 
    // std::string& data_str __assign__ operator

    *this = static_cast<char*>(&data_str[0]);
    return *this;
}

MyString & MyString::operator=(char symbol)
{ 
    // std::string& data_str __assign__ operator

    char* tmp = new char[2];
    tmp[0] = symbol;
    tmp[1] = '\0';
    *this = tmp;
    return *this;
}

MyString & MyString::operator=(MyString & another)
{
    // data_str __assign__ operator

    int cap1 = another.capacity();
    int cap2 = this->_capacity; 
    this->_size = another.size();
    this->_ptr = new char[this->_size +1];
    strncpy(this->_ptr, another.data(), this->_size+1);
    if (cap2>cap1) {this->_capacity = cap2;}
    else {this->_capacity = cap1;}
    return *this;
}

char& MyString::operator[](const size_t index)
{ 
    // index operator

    if(index <= this->_size){char* str = this->_ptr; return str[index];}
    else{char s = '\0'; return s;}
}

bool MyString::operator>(const MyString& another)
{
    // const MyString& another __gt__ operator

    return *this > another.data();
}
bool MyString::operator>(char* data_str)
{
    // char* data_str __gt__ operator

    for(size_t i=0; i<this->_size; i++)
    {
        if(this->_ptr[i] > data_str[i]){return true;}
        else if(this->_ptr[i] < data_str[i]){return false;}
        else{continue;}
    }
    return false;
}

bool MyString::operator<(const MyString& another)
{
    // MyString& another __lt__ operator

    return *this < another.data();
}

bool MyString::operator<(char* data_str)
{
    // char* data_str __lt__ operator

    return !(*this > data_str);
}

bool MyString::operator<=(const MyString& another)
{
    // MyString& another __le__ operator

    return *this <= another.data();
}

bool MyString::operator<=(char* data_str)
{
    // char* data_str __le__ operator

    if((*this == data_str)||(*this < data_str)){return true;}
    else{return false;}
}

bool MyString::operator>=(const MyString& another)
{
    // MyString& another __ge__ operator

    return *this >= another.data();
}

bool MyString::operator>=(char* data_str)
{
    // char* data_str __ge__ operator

    if((*this == data_str)||(*this > data_str)){return true;}
    else{return false;}
}

bool MyString::operator==(const MyString& another)
{
    // MyString& another __eq__ operator

    return *this == another.data();
}

bool MyString::operator==(char* data_str)
{
    // char* data_str __eq__ operator

    for (size_t i=0; i<this->_capacity; i++) 
    {
        if(this->_ptr[i] == data_str[i]){continue;}
        else{return false;}
    }
    return true;
}

bool MyString::operator==(char data_str)
{
    // char data_str __eq__ operator

    if(this->_ptr[0] == data_str){if(this->_ptr[1] != '\0'){return false;}}
    return true;
}

bool MyString::operator!=(const MyString& another)
{
    //  MyString& another __ne__ operator

    return !(*this == another.data());
}

bool MyString::operator!=(char* data_str)
{   // char* data_str __ne__ operator

    return !(*this == data_str);
}

char* MyString::data() const 
{ 
    // data function

    return this->_ptr;
}

char* MyString::c_str() const 
{ 
    // c_str pointer function

    return &(this->_ptr[0]);
}

size_t MyString::length() const 
{ 
    // same as size

    return size();
}

size_t MyString::size() const 
{ 
    // size function

    size_t i = 0;
    while (this->_ptr[i] != '\0') {
        i++;
    }
    return i;
}

size_t MyString::capacity() const 
{ 
    // capacity function

    return this->_capacity;
}

bool MyString::empty() const
{  
    // empty function

    return this->_size == 1 ? true : false;
}

void MyString::shrink_to_fit()
{ 
    // shrink_to_fit function

    this->_size = strlen(this->_ptr)+1;
    this->_capacity = this->_size;
}

void MyString::clear()
{  
    // remove all elements

    for(size_t i=0; i<this->_capacity; i++){this->_ptr[i] = '\0';}
}

ostream& operator<<(ostream& out, MyString& another)
{
    // << operator

    out << another.data();
    return out;
}

istream& operator>>(istream& in, MyString& another)
{
    // >>operator

    char c = 'a';
    int cnt = 0;
    while((c != '\n')&&(c != EOF))
    {
        if (in.tellg() == -1){break;}
        c = in.get();
        if (c!=255){another.append(1, c);}
        cnt+=1;
    }
    return in;
}

void MyString::insert(size_t index, size_t count, char symbol)
{ 
    // insert(size_t index, size_t count, char symbol) overload

    char* tmp = new char[2];
    tmp[0] = symbol;
    tmp[1] = '\0';
    for(size_t i=0; i<count; i++){insert(index, tmp);}
}

void MyString::insert(const size_t index, const char* string)
{
    // insert(const size_t index, const char* string) overload

    size_t len = strlen(string)+1;
    size_t len1 = strlen(this->_ptr)+1;
    char* tmp = new char[len1+1+len];
    size_t j = 0;
    for(size_t i=0; i<len1+len-1; i++)
    {
        if(i == index)
        {
            for(size_t k=0; k<len-1; k++){tmp[index+k] = string[k];}
            i = index + len - 2;
        }
        else
        {
            tmp[i] = this->_ptr[j];
            j++;
        }
    }
    this->_ptr = new char[len1+1+len];
    strncpy(this->_ptr, tmp, len1+1+len);
    if(this->_capacity < strlen(this->_ptr)){this->_capacity = length()+1;}
    this->_size = strlen(tmp)+1;
}

void MyString::insert(const size_t index, const char* string1, const size_t count)
{
     // insert(const size_t index, const char* string1, const size_t count) overload

    int cap = this->_capacity;
    if (string1[0]!='\0')
    {
        char string2[count+1];
        for (int i =0; i<count; i++){string2[i] = string1[i];}
        string2[count] = '\0';
        this->insert(index, string2);
        if(strlen(string2) >= this->_capacity){this->_capacity = length();}
        else{this->_capacity = cap;}
    }
}

void MyString::insert(const size_t index, std::string& data_str)
{ 
    // insert(const size_t index, std::string& data_str) overload

    this->insert(index, static_cast<char*>(&data_str[0]));
}

void MyString::insert(const size_t index, std::string& data_str, const size_t count)
{ 
    // insert(const size_t index, std::string& data_str, const size_t count) overload

    this->insert(index,static_cast<char*>(&data_str[0]), count);
}

void MyString::erase(size_t index, size_t count)
{ 
    // erase function

    if (index<strlen(this->_ptr))
    {
        char* tmp = new char[this->_capacity];
        strncpy(tmp, &(this->_ptr[index+count]), this->_size-index);
        for(size_t i=0; i<count; i++){this->_ptr[index+i] = '\0';}
        strcat(this->_ptr, tmp);
        this->_size = strlen(this->_ptr)+1;
    }
}

void MyString::append(size_t count, char symbol)
{ 
    // append(size_t count, char symbol) overload 
    
    this->insert(strlen(this->_ptr), count, symbol);
}

void MyString::append(const char* data_str)
{ 
    // append(const char* data_str) overload

    this->insert(strlen(this->_ptr), data_str);
}

void MyString::append(const char* data_str, const size_t index, const size_t count)
{ 
    // append(const char* data_str, const size_t index, const size_t count) overload

    char* tmp = new char[count+1];
    strncpy(tmp, &data_str[index], count);
    tmp[count] = '\0';
    this->insert(strlen(this->_ptr), tmp);

}

void MyString::append(std::string& data_str)
{ 
    // append(std::string& data_str) overload

    this->insert(strlen(this->_ptr), static_cast<char*>(&data_str[0]));
}

void MyString::append(std::string& data_str, const size_t index, const size_t count)
{ 
    // append(std::string& data_str, const size_t index, const size_t count) overload

    this->append(static_cast<char*>(&data_str[0]), index, count);
}

void MyString::replace(const size_t index, const size_t count, const char* data_str)
{ 
    // replace(const size_t index, const size_t count, const char* data_str) overload

    int capacity = this->_capacity;
    if(index <= this->_capacity)
    {
        if (count!=0){this->erase(index, count);}
        this->insert(index, data_str);
    }
    if (strlen(this->_ptr)>capacity){
    this->_capacity = strlen(this->_ptr);}
    else {this->_capacity = capacity;}
    this->_ptr[(strlen(this->_ptr))] = '\0';
}

void MyString::replace(const size_t index, const size_t count, std::string& data_str)
{ 
    // replace(const size_t index, const size_t count, std::string& data_str) overload

    if(index <= this->_capacity){this->replace(index, count, static_cast<char*>(&data_str[0]));}
}

MyString & MyString::substr(size_t index)
{ 
    // substr(size_t index) overload

    MyString tmp(this->_ptr+index, (strlen(this->_ptr))-index);
    *this = tmp;
    return *this;
}

MyString & MyString::substr(size_t index, size_t count)
{
    // substr(size_t index, size_t count) overload

    MyString tmp(this->_ptr+index, count);
    *this = tmp;
    return *this;
}

size_t MyString::find(const char* data_str)
{ 
    // find(const char* data_str) overload

    return this->find(data_str, 0);
}

size_t MyString::find(const char* data_str, const size_t index)
{ 
    // find(const char* data_str, const size_t index) overload

    if(strlen(data_str) <= this->_size)
    {
        size_t sym_counter = 0;
        size_t sym_i = 0;
        size_t j = 0;
        for(size_t i=index; i < this->_size; i++)
        {
            if(this->_ptr[i] == data_str[j])
            {
                sym_counter++;
                j++;
                if(sym_counter == 1){sym_i = i;}
                if(sym_counter == strlen(data_str)){return sym_i;}
            }
            else
            {
                sym_counter = 0;
                j = 0;
            }
        }
        return -1;
    }
    return -1;
}

size_t MyString::find(std::string& data_str)
{ 
    // find(std::string& data_str) overload

    return this->find(&data_str[0], 0);
}

size_t MyString::find(std::string& data_str, size_t index)
{ 
    // find(std::string& data_str, size_t index) overload

    return this->find(&data_str[0], index);
}