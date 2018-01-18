// Author Michael Shaffer
#include <boost/python.hpp>

bool sw = false;

char const* greet()
{	
	sw = !sw;
	if (sw)
		return "hello, world";
	else
		return "goodbye, world";
}

boost::python::object my_callback;

void set_callback(boost::python::object &callback)
{
	my_callback = callback;
}

void callback(void) 
{
	my_callback();
}

//void callbackArgs(boost::python::object &args)
void callbackArgs(boost::python::object &args) {
	my_callback(args, NULL);
}

BOOST_PYTHON_MODULE(BoostPythonTestLib)
{
    using namespace boost::python;
    def("greet", greet);
	def("set_callback", set_callback);
	def("callback", callback);
	def("callback", callbackArgs);
	
}