from collections import namedtuple

__version__ = '0.0.1dev0'

fname = "Olawale"
lname = "Oyeyipo"
full_name = "%s %s" % (fname, lname)

_Rec = namedtuple("Social", "Stackoverflow Github LinkedIn")
social = _Rec(
    stackoverflow="www.stackoverflow.com",
    github="www.github.com/oyeyipo",
    linkedin="linkedin.com/oyeyipo",
)
