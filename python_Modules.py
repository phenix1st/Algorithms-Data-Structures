"""	
__future__	Future statement definitions
__main__	The environment where top-level code is run. Covers command-line interfaces, import-time behavior, and ``__name__ == '__main__'``.
_thread	Low-level threading API.
_tkinter	A binary module that contains the low-level interface to Tcl/Tk.
 	
a	
abc	Abstract base classes according to :pep:`3119`.
aifc	Deprecated: Removed in 3.13.
argparse	Command-line option and argument parsing library.
array	Space efficient arrays of uniformly typed numeric values.
ast	Abstract Syntax Tree classes and manipulation.
asynchat	Deprecated: Removed in 3.12.
asyncio	Asynchronous I/O.
asyncore	Deprecated: Removed in 3.12.
atexit	Register and execute cleanup functions.
audioop	Deprecated: Removed in 3.13.
 	
b	
base64	RFC 4648: Base16, Base32, Base64 Data Encodings; Base85 and Ascii85
bdb	Debugger framework.
binascii	Tools for converting between binary and various ASCII-encoded binary representations.
bisect	Array bisection algorithms for binary searching.
builtins	The module that provides the built-in namespace.
bz2	Interfaces for bzip2 compression and decompression.
 	
c	
calendar	Functions for working with calendars, including some emulation of the Unix cal program.
cgi	Deprecated: Removed in 3.13.
cgitb	Deprecated: Removed in 3.13.
chunk	Deprecated: Removed in 3.13.
cmath	Mathematical functions for complex numbers.
cmd	Build line-oriented command interpreters.
code	Facilities to implement read-eval-print loops.
codecs	Encode and decode data and streams.
codeop	Compile (possibly incomplete) Python code.
-	collections	Container datatypes
colorsys	Conversion functions between RGB and other color systems.
compileall	Tools for byte-compiling all Python source files in a directory tree.
-	concurrent	
configparser	Configuration file parser.
contextlib	Utilities for with-statement contexts.
contextvars	Context Variables
copy	Shallow and deep copy operations.
copyreg	Register pickle support functions.
cProfile	
crypt	Deprecated: Removed in 3.13.
csv	Write and read tabular data to and from delimited files.
ctypes	A foreign function library for Python.
-	curses (Unix)	An interface to the curses library, providing portable terminal handling.
 	
d	
dataclasses	Generate special methods on user-defined classes.
datetime	Basic date and time types.
-	dbm	Interfaces to various Unix "database" formats.
decimal	Implementation of the General Decimal Arithmetic Specification.
difflib	Helpers for computing differences between objects.
dis	Disassembler for Python bytecode.
distutils	Deprecated: Removed in 3.12.
doctest	Test pieces of code within docstrings.
 	
e	
-	email	Package supporting the parsing, manipulating, and generating email messages.
-	encodings	
ensurepip	Bootstrapping the "pip" installer into an existing Python installation or virtual environment.
enum	Implementation of an enumeration class.
errno	Standard errno system symbols.
 	
f	
faulthandler	Dump the Python traceback.
fcntl (Unix)	The fcntl() and ioctl() system calls.
filecmp	Compare files efficiently.
fileinput	Loop over standard input or a list of files.
fnmatch	Unix shell style filename pattern matching.
fractions	Rational numbers.
ftplib	FTP protocol client (requires sockets).
functools	Higher-order functions and operations on callable objects.
 	
g	
gc	Interface to the cycle-detecting garbage collector.
getopt	Portable parser for command line options; support both short and long option names.
getpass	Portable reading of passwords and retrieval of the userid.
gettext	Multilingual internationalization services.
glob	Unix shell style pathname pattern expansion.
graphlib	Functionality to operate with graph-like structures
grp (Unix)	The group database (getgrnam() and friends).
gzip	Interfaces for gzip compression and decompression using file objects.
 	
h	
hashlib	Secure hash and message digest algorithms.
heapq	Heap queue algorithm (a.k.a. priority queue).
hmac	Keyed-Hashing for Message Authentication (HMAC) implementation
-	html	Helpers for manipulating HTML.
-	http	HTTP status codes and messages
 	
i	
idlelib	Implementation package for the IDLE shell/editor.
imaplib	IMAP4 protocol client (requires sockets).
imghdr	Deprecated: Removed in 3.13.
imp	Deprecated: Removed in 3.12.
-	importlib	The implementation of the import machinery.
inspect	Extract information and source code from live objects.
io	Core tools for working with streams.
ipaddress	IPv4/IPv6 manipulation library.
itertools	Functions creating iterators for efficient looping.
 	
j	
-	json	Encode and decode the JSON format.
 	
k	
keyword	Test whether a string is a keyword in Python.
 	
l	
linecache	Provides random access to individual lines from text files.
locale	Internationalization services.
-	logging	Flexible event logging system for applications.
lzma	A Python wrapper for the liblzma compression library.
 	
m	
mailbox	Manipulate mailboxes in various formats
mailcap	Deprecated: Removed in 3.13.
marshal	Convert Python objects to streams of bytes and back (with different constraints).
math	Mathematical functions (sin() etc.).
mimetypes	Mapping of filename extensions to MIME types.
mmap	Interface to memory-mapped files for Unix and Windows.
modulefinder	Find modules used by a script.
msilib	Deprecated: Removed in 3.13.
msvcrt (Windows)	Miscellaneous useful routines from the MS VC++ runtime.
-	multiprocessing	Process-based parallelism.
 	
n	
netrc	Loading of .netrc files.
nis	Deprecated: Removed in 3.13.
nntplib	Deprecated: Removed in 3.13.
numbers	Numeric abstract base classes (Complex, Real, Integral, etc.).
 	
o	
operator	Functions corresponding to the standard operators.
optparse	Command-line option parsing library.
-	os	Miscellaneous operating system interfaces.
ossaudiodev	Deprecated: Removed in 3.13.
 	
p	
pathlib	Object-oriented filesystem paths
pdb	The Python debugger for interactive interpreters.
pickle	Convert Python objects to streams of bytes and back.
pickletools	Contains extensive comments about the pickle protocols and pickle-machine opcodes, as well as some useful functions.
pipes	Deprecated: Removed in 3.13.
pkgutil	Utilities for the import system.
platform	Retrieves as much platform identifying data as possible.
plistlib	Generate and parse Apple plist files.
poplib	POP3 protocol client (requires sockets).
posix (Unix)	The most common POSIX system calls (normally used via module os).
pprint	Data pretty printer.
profile	Python source profiler.
pstats	Statistics object for use with the profiler.
pty (Unix)	Pseudo-Terminal Handling for Unix.
pwd (Unix)	The password database (getpwnam() and friends).
py_compile	Generate byte-code files from Python source files.
pyclbr	Supports information extraction for a Python module browser.
pydoc	Documentation generator and online help system.
 	
q	
queue	A synchronized queue class.
quopri	Encode and decode files using the MIME quoted-printable encoding.
 	
r	
random	Generate pseudo-random numbers with various common distributions.
re	Regular expression operations.
readline (Unix)	GNU readline support for Python.
reprlib	Alternate repr() implementation with size limits.
resource (Unix)	An interface to provide resource usage information on the current process.
rlcompleter	Python identifier completion, suitable for the GNU readline library.
runpy	Locate and run Python modules without importing them first.
 	
s	
sched	General purpose event scheduler.
secrets	Generate secure random numbers for managing secrets.
select	Wait for I/O completion on multiple streams.
selectors	High-level I/O multiplexing.
shelve	Python object persistence.
shlex	Simple lexical analysis for Unix shell-like languages.
shutil	High-level file operations, including copying.
signal	Set handlers for asynchronous events.
site	Module responsible for site-specific configuration.
sitecustomize	
smtpd	Deprecated: Removed in 3.12.
smtplib	SMTP protocol client (requires sockets).
sndhdr	Deprecated: Removed in 3.13.
socket	Low-level networking interface.
socketserver	A framework for network servers.
spwd	Deprecated: Removed in 3.13.
sqlite3	A DB-API 2.0 implementation using SQLite 3.x.
ssl	TLS/SSL wrapper for socket objects
stat	Utilities for interpreting the results of os.stat(), os.lstat() and os.fstat().
statistics	Mathematical statistics functions
string	Common string operations.
stringprep	String preparation, as per RFC 3453
struct	Interpret bytes as packed binary data.
subprocess	Subprocess management.
sunau	Deprecated: Removed in 3.13.
symtable	Interface to the compiler's internal symbol tables.
-	sys	Access system-specific parameters and functions.
sysconfig	Python's configuration information
syslog (Unix)	An interface to the Unix syslog library routines.
 	
t	
tabnanny	Tool for detecting white space related problems in Python source files in a directory tree.
tarfile	Read and write tar-format archive files.
telnetlib	Deprecated: Removed in 3.13.
tempfile	Generate temporary files and directories.
termios (Unix)	POSIX style tty control.
-	test	Regression tests package containing the testing suite for Python.
textwrap	Text wrapping and filling
threading	Thread-based parallelism.
time	Time access and conversions.
timeit	Measure the execution time of small code snippets.
-	tkinter	Interface to Tcl/Tk for graphical user interfaces
token	Constants representing terminal nodes of the parse tree.
tokenize	Lexical scanner for Python source code.
tomllib	Parse TOML files.
trace	Trace or track Python statement execution.
traceback	Print or retrieve a stack traceback.
tracemalloc	Trace memory allocations.
tty (Unix)	Utility functions that perform common terminal control operations.
turtle	An educational framework for simple graphics applications
turtledemo	A viewer for example turtle scripts
types	Names for built-in types.
typing	Support for type hints (see :pep:`484`).
 	
u	
unicodedata	Access the Unicode Database.
-	unittest	Unit testing framework for Python.
-	urllib	
usercustomize	
uu	Deprecated: Removed in 3.13.
uuid	UUID objects (universally unique identifiers) according to RFC 4122
 	
v	
venv	Creation of virtual environments.
 	
w	
warnings	Issue warning messages and control their disposition.
wave	Provide an interface to the WAV sound format.
weakref	Support for weak references and weak dictionaries.
webbrowser	Easy-to-use controller for web browsers.
winreg (Windows)	Routines and objects for manipulating the Windows registry.
winsound (Windows)	Access to the sound-playing machinery for Windows.
-	wsgiref	WSGI Utilities and Reference Implementation.
 	
x	
xdrlib	Deprecated: Removed in 3.13.
-	xml	Package containing XML processing modules
-	xmlrpc	Server and client modules implementing XML-RPC.
 	
z	
zipapp	Manage executable Python zip archives
zipfile	Read and write ZIP-format archive files.
zipimport	Support for importing Python modules from ZIP archives.
zlib	Low-level interface to compression and decompression routines compatible with gzip.
zoneinfo	IANA time zone support
"""