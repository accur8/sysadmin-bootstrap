#!/usr/bin/env python3

# built 2022-11-06 

import sys

import math as python_lib_Math
import math as Math
from os import path as python_lib_os_Path
import inspect as python_lib_Inspect
import sched as a8_PySched
import sys as python_lib_Sys
from threading import Thread as python_lib_threading_Thread
import time as python_lib_Time
import shutil as a8_PyShutil2
import os as a8_PyOs2
import builtins as python_lib_Builtins
import os as python_lib_Os
import functools as python_lib_Functools
import io as python_lib_Io
import json as python_lib_Json
import random as python_lib_Random
import re as python_lib_Re
import socket as python_lib_Socket
import ssl as python_lib_Ssl
import subprocess as python_lib_Subprocess
import timeit as python_lib_Timeit
import traceback as python_lib_Traceback
from datetime import datetime as python_lib_datetime_Datetime
from datetime import timezone as python_lib_datetime_Timezone
from io import StringIO as python_lib_io_StringIO
from socket import socket as python_lib_socket_Socket
from ssl import SSLContext as python_lib_ssl_SSLContext
from subprocess import Popen as python_lib_subprocess_Popen
import urllib.parse as python_lib_urllib_Parse
from threading import Semaphore as Lock
from threading import RLock as sys_thread__Mutex_NativeRLock
import threading


class _hx_AnonObject:
    _hx_disable_getattr = False
    def __init__(self, fields):
        self.__dict__ = fields
    def __repr__(self):
        return repr(self.__dict__)
    def __contains__(self, item):
        return item in self.__dict__
    def __getitem__(self, item):
        return self.__dict__[item]
    def __getattr__(self, name):
        if (self._hx_disable_getattr):
            raise AttributeError('field does not exist')
        else:
            return None
    def _hx_hasattr(self,field):
        self._hx_disable_getattr = True
        try:
            getattr(self, field)
            self._hx_disable_getattr = False
            return True
        except AttributeError:
            self._hx_disable_getattr = False
            return False



class Enum:
    _hx_class_name = "Enum"
    _hx_is_interface = "False"
    __slots__ = ("tag", "index", "params")
    _hx_fields = ["tag", "index", "params"]
    _hx_methods = ["__str__"]

    def __init__(self,tag,index,params):
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/EnumImpl.hx:39
        self.tag = tag
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/EnumImpl.hx:40
        self.index = index
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/EnumImpl.hx:41
        self.params = params

    def __str__(self):
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/EnumImpl.hx:46
        if (self.params is None):
            return self.tag
        else:
            return self.tag + '(' + (', '.join(str(v) for v in self.params)) + ')'

Enum._hx_class = Enum


class Class: pass


class Date:
    _hx_class_name = "Date"
    _hx_is_interface = "False"
    __slots__ = ("date", "dateUTC")
    _hx_fields = ["date", "dateUTC"]
    _hx_methods = ["toString"]
    _hx_statics = ["now", "fromTime", "makeLocal"]

    def __init__(self,year,month,day,hour,_hx_min,sec):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Date.hx:30
        self.dateUTC = None
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Date.hx:33
        if (year < python_lib_datetime_Datetime.min.year):
            year = python_lib_datetime_Datetime.min.year
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Date.hx:35
        if (day == 0):
            day = 1
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Date.hx:37
        self.date = Date.makeLocal(python_lib_datetime_Datetime(year,(month + 1),day,hour,_hx_min,sec,0))
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Date.hx:38
        self.dateUTC = self.date.astimezone(python_lib_datetime_Timezone.utc)

    def toString(self):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Date.hx:106
        return self.date.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def now():
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Date.hx:110
        d = Date(2000,0,1,0,0,0)
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Date.hx:111
        d.date = Date.makeLocal(python_lib_datetime_Datetime.now())
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Date.hx:112
        d.dateUTC = d.date.astimezone(python_lib_datetime_Timezone.utc)
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Date.hx:113
        return d

    @staticmethod
    def fromTime(t):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Date.hx:117
        d = Date(2000,0,1,0,0,0)
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Date.hx:118
        d.date = Date.makeLocal(python_lib_datetime_Datetime.fromtimestamp((t / 1000.0)))
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Date.hx:119
        d.dateUTC = d.date.astimezone(python_lib_datetime_Timezone.utc)
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Date.hx:120
        return d

    @staticmethod
    def makeLocal(date):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Date.hx:124
        try:
            return date.astimezone()
        except BaseException as _g:
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/Date.hx:126
            None
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/Date.hx:129
            tzinfo = python_lib_datetime_Datetime.now(python_lib_datetime_Timezone.utc).astimezone().tzinfo
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/Date.hx:130
            return date.replace(**python__KwArgs_KwArgs_Impl_.fromT(_hx_AnonObject({'tzinfo': tzinfo})))

Date._hx_class = Date


class EReg:
    _hx_class_name = "EReg"
    _hx_is_interface = "False"
    __slots__ = ("pattern", "matchObj", "_hx_global")
    _hx_fields = ["pattern", "matchObj", "global"]

    def __init__(self,r,opt):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/EReg.hx:31
        self.matchObj = None
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/EReg.hx:35
        self._hx_global = False
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/EReg.hx:36
        options = 0
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/EReg.hx:37
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/EReg.hx:37
        _g = 0
        _g1 = len(opt)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/EReg.hx:38
            c = (-1 if ((i >= len(opt))) else ord(opt[i]))
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/EReg.hx:39
            if (c == 109):
                options = (options | python_lib_Re.M)
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/EReg.hx:41
            if (c == 105):
                options = (options | python_lib_Re.I)
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/EReg.hx:43
            if (c == 115):
                options = (options | python_lib_Re.S)
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/EReg.hx:45
            if (c == 117):
                options = (options | python_lib_Re.U)
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/EReg.hx:47
            if (c == 103):
                self._hx_global = True
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/EReg.hx:50
        self.pattern = python_lib_Re.compile(r,options)

EReg._hx_class = EReg


class Lambda:
    _hx_class_name = "Lambda"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["array", "exists", "iter", "find"]

    @staticmethod
    def array(it):
        # /Users/glen/bin/haxe-4.2.5/std/Lambda.hx:46
        a = list()
        # /Users/glen/bin/haxe-4.2.5/std/Lambda.hx:47
        # /Users/glen/bin/haxe-4.2.5/std/Lambda.hx:47
        i = HxOverrides.iterator(it)
        while i.hasNext():
            i1 = i.next()
            # /Users/glen/bin/haxe-4.2.5/std/Lambda.hx:48
            a.append(i1)
        # /Users/glen/bin/haxe-4.2.5/std/Lambda.hx:49
        return a

    @staticmethod
    def exists(it,f):
        # /Users/glen/bin/haxe-4.2.5/std/Lambda.hx:126
        # /Users/glen/bin/haxe-4.2.5/std/Lambda.hx:126
        x = HxOverrides.iterator(it)
        while x.hasNext():
            x1 = x.next()
            # /Users/glen/bin/haxe-4.2.5/std/Lambda.hx:127
            if f(x1):
                return True
        # /Users/glen/bin/haxe-4.2.5/std/Lambda.hx:129
        return False

    @staticmethod
    def iter(it,f):
        # /Users/glen/bin/haxe-4.2.5/std/Lambda.hx:157
        x = HxOverrides.iterator(it)
        while x.hasNext():
            x1 = x.next()
            # /Users/glen/bin/haxe-4.2.5/std/Lambda.hx:158
            f(x1)

    @staticmethod
    def find(it,f):
        # /Users/glen/bin/haxe-4.2.5/std/Lambda.hx:256
        # /Users/glen/bin/haxe-4.2.5/std/Lambda.hx:256
        v = HxOverrides.iterator(it)
        while v.hasNext():
            v1 = v.next()
            # /Users/glen/bin/haxe-4.2.5/std/Lambda.hx:257
            if f(v1):
                return v1
        # /Users/glen/bin/haxe-4.2.5/std/Lambda.hx:260
        return None
Lambda._hx_class = Lambda


class Reflect:
    _hx_class_name = "Reflect"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["field", "setField", "isFunction", "compareMethods", "copy"]

    @staticmethod
    def field(o,field):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Reflect.hx:43
        return python_Boot.field(o,field)

    @staticmethod
    def setField(o,field,value):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Reflect.hx:48
        setattr(o,(("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field)),value)

    @staticmethod
    def isFunction(f):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Reflect.hx:84
        if (not ((python_lib_Inspect.isfunction(f) or python_lib_Inspect.ismethod(f)))):
            return python_Boot.hasField(f,"func_code")
        else:
            return True

    @staticmethod
    def compareMethods(f1,f2):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Reflect.hx:98
        if HxOverrides.eq(f1,f2):
            return True
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Reflect.hx:100
        if (isinstance(f1,python_internal_MethodClosure) and isinstance(f2,python_internal_MethodClosure)):
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/Reflect.hx:101
            m1 = f1
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/Reflect.hx:102
            m2 = f2
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/Reflect.hx:103
            if HxOverrides.eq(m1.obj,m2.obj):
                return (m1.func == m2.func)
            else:
                return False
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Reflect.hx:105
        if ((not Reflect.isFunction(f1)) or (not Reflect.isFunction(f2))):
            return False
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Reflect.hx:108
        return False

    @staticmethod
    def copy(o):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Reflect.hx:131
        if (o is None):
            return None
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Reflect.hx:133
        o2 = _hx_AnonObject({})
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Reflect.hx:134
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Reflect.hx:134
        _g = 0
        _g1 = python_Boot.fields(o)
        while (_g < len(_g1)):
            f = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/Reflect.hx:135
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/Reflect.hx:135
            value = Reflect.field(o,f)
            setattr(o2,(("_hx_" + f) if ((f in python_Boot.keywords)) else (("_hx_" + f) if (((((len(f) > 2) and ((ord(f[0]) == 95))) and ((ord(f[1]) == 95))) and ((ord(f[(len(f) - 1)]) != 95)))) else f)),value)
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Reflect.hx:136
        return o2
Reflect._hx_class = Reflect


class Std:
    _hx_class_name = "Std"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["downcast", "isOfType", "string", "parseInt"]

    @staticmethod
    def downcast(value,c):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Std.hx:35
        try:
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/Std.hx:36
            tmp = None
            if (not isinstance(value,c)):
                if c._hx_is_interface:
                    cls = c
                    loop = None
                    def _hx_local_1(intf):
                        f = (intf._hx_interfaces if (hasattr(intf,"_hx_interfaces")) else [])
                        if (f is not None):
                            _g = 0
                            while (_g < len(f)):
                                i = (f[_g] if _g >= 0 and _g < len(f) else None)
                                _g = (_g + 1)
                                if (i == cls):
                                    return True
                                else:
                                    l = loop(i)
                                    if l:
                                        return True
                            return False
                        else:
                            return False
                    loop = _hx_local_1
                    currentClass = value.__class__
                    result = False
                    while (currentClass is not None):
                        if loop(currentClass):
                            result = True
                            break
                        currentClass = python_Boot.getSuperClass(currentClass)
                    tmp = result
                else:
                    tmp = False
            else:
                tmp = True
            if tmp:
                return value
            else:
                return None
        except BaseException as _g:
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/Std.hx:37
            None
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/Std.hx:38
            return None

    @staticmethod
    def isOfType(v,t):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Std.hx:61
        if ((v is None) and ((t is None))):
            return False
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Std.hx:64
        if (t is None):
            return False
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Std.hx:67
        if ((type(t) == type) and (t == Dynamic)):
            return (v is not None)
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Std.hx:70
        isBool = isinstance(v,bool)
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Std.hx:72
        if (((type(t) == type) and (t == Bool)) and isBool):
            return True
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Std.hx:75
        if ((((not isBool) and (not ((type(t) == type) and (t == Bool)))) and ((type(t) == type) and (t == Int))) and isinstance(v,int)):
            return True
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Std.hx:78
        vIsFloat = isinstance(v,float)
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Std.hx:80
        tmp = None
        tmp1 = None
        if (((not isBool) and vIsFloat) and ((type(t) == type) and (t == Int))):
            f = v
            tmp1 = (((f != Math.POSITIVE_INFINITY) and ((f != Math.NEGATIVE_INFINITY))) and (not python_lib_Math.isnan(f)))
        else:
            tmp1 = False
        if tmp1:
            tmp1 = None
            try:
                tmp1 = int(v)
            except BaseException as _g:
                # /Users/glen/bin/haxe-4.2.5/std/python/_std/Std.hx:128
                None
                # /Users/glen/bin/haxe-4.2.5/std/python/_std/Std.hx:80
                tmp1 = None
            tmp = (v == tmp1)
        else:
            tmp = False
        if ((tmp and ((v <= 2147483647))) and ((v >= -2147483648))):
            return True
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Std.hx:84
        if (((not isBool) and ((type(t) == type) and (t == Float))) and isinstance(v,(float, int))):
            return True
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Std.hx:88
        if ((type(t) == type) and (t == str)):
            return isinstance(v,str)
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Std.hx:91
        isEnumType = ((type(t) == type) and (t == Enum))
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Std.hx:92
        if ((isEnumType and python_lib_Inspect.isclass(v)) and hasattr(v,"_hx_constructs")):
            return True
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Std.hx:95
        if isEnumType:
            return False
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Std.hx:98
        isClassType = ((type(t) == type) and (t == Class))
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Std.hx:99
        if ((((isClassType and (not isinstance(v,Enum))) and python_lib_Inspect.isclass(v)) and hasattr(v,"_hx_class_name")) and (not hasattr(v,"_hx_constructs"))):
            return True
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Std.hx:106
        if isClassType:
            return False
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Std.hx:109
        tmp = None
        try:
            tmp = isinstance(v,t)
        except BaseException as _g:
            None
            tmp = False
        if tmp:
            return True
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Std.hx:113
        if python_lib_Inspect.isclass(t):
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/Std.hx:114
            cls = t
            loop = None
            def _hx_local_1(intf):
                f = (intf._hx_interfaces if (hasattr(intf,"_hx_interfaces")) else [])
                if (f is not None):
                    _g = 0
                    while (_g < len(f)):
                        i = (f[_g] if _g >= 0 and _g < len(f) else None)
                        _g = (_g + 1)
                        if (i == cls):
                            return True
                        else:
                            l = loop(i)
                            if l:
                                return True
                    return False
                else:
                    return False
            loop = _hx_local_1
            currentClass = v.__class__
            result = False
            while (currentClass is not None):
                if loop(currentClass):
                    result = True
                    break
                currentClass = python_Boot.getSuperClass(currentClass)
            return result
        else:
            return False

    @staticmethod
    def string(s):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Std.hx:122
        return python_Boot.toString1(s,"")

    @staticmethod
    def parseInt(x):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Std.hx:134
        if (x is None):
            return None
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Std.hx:136
        try:
            return int(x)
        except BaseException as _g:
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/Std.hx:138
            None
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/Std.hx:139
            base = 10
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/Std.hx:140
            _hx_len = len(x)
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/Std.hx:141
            foundCount = 0
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/Std.hx:142
            sign = 0
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/Std.hx:143
            firstDigitIndex = 0
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/Std.hx:144
            lastDigitIndex = -1
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/Std.hx:145
            previous = 0
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/Std.hx:147
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/Std.hx:147
            _g = 0
            _g1 = _hx_len
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                # /Users/glen/bin/haxe-4.2.5/std/python/_std/Std.hx:148
                c = (-1 if ((i >= len(x))) else ord(x[i]))
                # /Users/glen/bin/haxe-4.2.5/std/python/_std/Std.hx:149
                if (((c > 8) and ((c < 14))) or ((c == 32))):
                    # /Users/glen/bin/haxe-4.2.5/std/python/_std/Std.hx:151
                    if (foundCount > 0):
                        return None
                    # /Users/glen/bin/haxe-4.2.5/std/python/_std/Std.hx:154
                    continue
                else:
                    # /Users/glen/bin/haxe-4.2.5/std/python/_std/Std.hx:149
                    c1 = c
                    # /Users/glen/bin/haxe-4.2.5/std/python/_std/Std.hx:157
                    if (c1 == 43):
                        if (foundCount == 0):
                            sign = 1
                        elif (not (((48 <= c) and ((c <= 57))))):
                            if (not (((base == 16) and ((((97 <= c) and ((c <= 122))) or (((65 <= c) and ((c <= 90))))))))):
                                break
                    elif (c1 == 45):
                        if (foundCount == 0):
                            sign = -1
                        elif (not (((48 <= c) and ((c <= 57))))):
                            if (not (((base == 16) and ((((97 <= c) and ((c <= 122))) or (((65 <= c) and ((c <= 90))))))))):
                                break
                    elif (c1 == 48):
                        if (not (((foundCount == 0) or (((foundCount == 1) and ((sign != 0))))))):
                            if (not (((48 <= c) and ((c <= 57))))):
                                if (not (((base == 16) and ((((97 <= c) and ((c <= 122))) or (((65 <= c) and ((c <= 90))))))))):
                                    break
                    elif ((c1 == 120) or ((c1 == 88))):
                        if ((previous == 48) and ((((foundCount == 1) and ((sign == 0))) or (((foundCount == 2) and ((sign != 0))))))):
                            base = 16
                        elif (not (((48 <= c) and ((c <= 57))))):
                            if (not (((base == 16) and ((((97 <= c) and ((c <= 122))) or (((65 <= c) and ((c <= 90))))))))):
                                break
                    elif (not (((48 <= c) and ((c <= 57))))):
                        if (not (((base == 16) and ((((97 <= c) and ((c <= 122))) or (((65 <= c) and ((c <= 90))))))))):
                            break
                # /Users/glen/bin/haxe-4.2.5/std/python/_std/Std.hx:167
                if (((foundCount == 0) and ((sign == 0))) or (((foundCount == 1) and ((sign != 0))))):
                    firstDigitIndex = i
                # /Users/glen/bin/haxe-4.2.5/std/python/_std/Std.hx:170
                foundCount = (foundCount + 1)
                # /Users/glen/bin/haxe-4.2.5/std/python/_std/Std.hx:171
                lastDigitIndex = i
                # /Users/glen/bin/haxe-4.2.5/std/python/_std/Std.hx:172
                previous = c
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/Std.hx:174
            if (firstDigitIndex <= lastDigitIndex):
                # /Users/glen/bin/haxe-4.2.5/std/python/_std/Std.hx:175
                digits = HxString.substring(x,firstDigitIndex,(lastDigitIndex + 1))
                # /Users/glen/bin/haxe-4.2.5/std/python/_std/Std.hx:176
                try:
                    return (((-1 if ((sign == -1)) else 1)) * int(digits,base))
                except BaseException as _g:
                    return None
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/Std.hx:182
            return None
Std._hx_class = Std


class Float: pass


class Int: pass


class Bool: pass


class Dynamic: pass


class StringBuf:
    _hx_class_name = "StringBuf"
    _hx_is_interface = "False"
    __slots__ = ("b",)
    _hx_fields = ["b"]
    _hx_methods = ["get_length"]

    def __init__(self):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/StringBuf.hx:31
        self.b = python_lib_io_StringIO()

    def get_length(self):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/StringBuf.hx:37
        pos = self.b.tell()
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/StringBuf.hx:38
        self.b.seek(0,2)
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/StringBuf.hx:39
        _hx_len = self.b.tell()
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/StringBuf.hx:40
        self.b.seek(pos,0)
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/StringBuf.hx:41
        return _hx_len

StringBuf._hx_class = StringBuf


class StringTools:
    _hx_class_name = "StringTools"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["isSpace", "ltrim", "rtrim", "lpad", "rpad"]

    @staticmethod
    def isSpace(s,pos):
        # /Users/glen/bin/haxe-4.2.5/std/StringTools.hx:280
        if (((len(s) == 0) or ((pos < 0))) or ((pos >= len(s)))):
            return False
        # /Users/glen/bin/haxe-4.2.5/std/StringTools.hx:283
        c = HxString.charCodeAt(s,pos)
        # /Users/glen/bin/haxe-4.2.5/std/StringTools.hx:284
        if (not (((c > 8) and ((c < 14))))):
            return (c == 32)
        else:
            return True

    @staticmethod
    def ltrim(s):
        # /Users/glen/bin/haxe-4.2.5/std/StringTools.hx:300
        l = len(s)
        # /Users/glen/bin/haxe-4.2.5/std/StringTools.hx:301
        r = 0
        # /Users/glen/bin/haxe-4.2.5/std/StringTools.hx:302
        while ((r < l) and StringTools.isSpace(s,r)):
            r = (r + 1)
        # /Users/glen/bin/haxe-4.2.5/std/StringTools.hx:305
        if (r > 0):
            return HxString.substr(s,r,(l - r))
        else:
            return s

    @staticmethod
    def rtrim(s):
        # /Users/glen/bin/haxe-4.2.5/std/StringTools.hx:325
        l = len(s)
        # /Users/glen/bin/haxe-4.2.5/std/StringTools.hx:326
        r = 0
        # /Users/glen/bin/haxe-4.2.5/std/StringTools.hx:327
        while ((r < l) and StringTools.isSpace(s,((l - r) - 1))):
            r = (r + 1)
        # /Users/glen/bin/haxe-4.2.5/std/StringTools.hx:330
        if (r > 0):
            return HxString.substr(s,0,(l - r))
        else:
            return s

    @staticmethod
    def lpad(s,c,l):
        # /Users/glen/bin/haxe-4.2.5/std/StringTools.hx:366
        if (len(c) <= 0):
            return s
        # /Users/glen/bin/haxe-4.2.5/std/StringTools.hx:369
        buf = StringBuf()
        # /Users/glen/bin/haxe-4.2.5/std/StringTools.hx:370
        l = (l - len(s))
        # /Users/glen/bin/haxe-4.2.5/std/StringTools.hx:371
        while (buf.get_length() < l):
            # /Users/glen/bin/haxe-4.2.5/std/StringTools.hx:372
            s1 = Std.string(c)
            buf.b.write(s1)
        # /Users/glen/bin/haxe-4.2.5/std/StringTools.hx:374
        # /Users/glen/bin/haxe-4.2.5/std/StringTools.hx:374
        s1 = Std.string(s)
        buf.b.write(s1)
        # /Users/glen/bin/haxe-4.2.5/std/StringTools.hx:375
        return buf.b.getvalue()

    @staticmethod
    def rpad(s,c,l):
        # /Users/glen/bin/haxe-4.2.5/std/StringTools.hx:391
        if (len(c) <= 0):
            return s
        # /Users/glen/bin/haxe-4.2.5/std/StringTools.hx:394
        buf = StringBuf()
        # /Users/glen/bin/haxe-4.2.5/std/StringTools.hx:395
        # /Users/glen/bin/haxe-4.2.5/std/StringTools.hx:395
        s1 = Std.string(s)
        buf.b.write(s1)
        # /Users/glen/bin/haxe-4.2.5/std/StringTools.hx:396
        while (buf.get_length() < l):
            # /Users/glen/bin/haxe-4.2.5/std/StringTools.hx:397
            s = Std.string(c)
            buf.b.write(s)
        # /Users/glen/bin/haxe-4.2.5/std/StringTools.hx:399
        return buf.b.getvalue()
StringTools._hx_class = StringTools


class sys_FileSystem:
    _hx_class_name = "sys.FileSystem"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["exists", "fullPath", "isDirectory", "createDirectory", "deleteFile", "readDirectory"]

    @staticmethod
    def exists(path):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/FileSystem.hx:31
        return python_lib_os_Path.exists(path)

    @staticmethod
    def fullPath(relPath):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/FileSystem.hx:56
        return python_lib_os_Path.realpath(relPath)

    @staticmethod
    def isDirectory(path):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/FileSystem.hx:66
        return python_lib_os_Path.isdir(path)

    @staticmethod
    def createDirectory(path):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/FileSystem.hx:70
        python_lib_Os.makedirs(path,511,True)

    @staticmethod
    def deleteFile(path):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/FileSystem.hx:74
        python_lib_Os.remove(path)

    @staticmethod
    def readDirectory(path):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/FileSystem.hx:82
        return python_lib_Os.listdir(path)
sys_FileSystem._hx_class = sys_FileSystem


class Sys:
    _hx_class_name = "Sys"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["environ", "get_environ", "exit", "environment", "systemName", "_programPath", "programPath"]
    environ = None

    @staticmethod
    def get_environ():
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Sys.hx:33
        _g = Sys.environ
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Sys.hx:34
        if (_g is None):
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/Sys.hx:35
            environ = haxe_ds_StringMap()
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/Sys.hx:36
            env = python_lib_Os.environ
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/Sys.hx:37
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/Sys.hx:37
            key = python_HaxeIterator(iter(env.keys()))
            while key.hasNext():
                key1 = key.next()
                # /Users/glen/bin/haxe-4.2.5/std/python/_std/Sys.hx:38
                # /Users/glen/bin/haxe-4.2.5/std/python/_std/Sys.hx:38
                value = env.get(key1,None)
                environ.h[key1] = value
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/Sys.hx:40
            def _hx_local_1():
                # /Users/glen/bin/haxe-4.2.5/std/python/_std/Sys.hx:40
                def _hx_local_0():
                    # /Users/glen/bin/haxe-4.2.5/std/python/_std/Sys.hx:40
                    Sys.environ = environ
                    return Sys.environ
                return _hx_local_0()
            return _hx_local_1()
        else:
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/Sys.hx:41
            env = _g
            return env

    @staticmethod
    def exit(code):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Sys.hx:50
        python_lib_Sys.exit(code)

    @staticmethod
    def environment():
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Sys.hx:76
        return Sys.get_environ()

    @staticmethod
    def systemName():
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Sys.hx:96
        _g = python_lib_Sys.platform
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Sys.hx:97
        x = _g
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Sys.hx:96
        if x.startswith("linux"):
            return "Linux"
        else:
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/Sys.hx:96
            _g1 = _g
            _hx_local_0 = len(_g1)
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/Sys.hx:100
            if (_hx_local_0 == 5):
                if (_g1 == "win32"):
                    return "Windows"
                else:
                    raise haxe_Exception.thrown("not supported platform")
            elif (_hx_local_0 == 6):
                if (_g1 == "cygwin"):
                    return "Windows"
                elif (_g1 == "darwin"):
                    return "Mac"
                else:
                    raise haxe_Exception.thrown("not supported platform")
            else:
                raise haxe_Exception.thrown("not supported platform")

    @staticmethod
    def programPath():
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Sys.hx:125
        return Sys._programPath
Sys._hx_class = Sys

class ValueType(Enum):
    __slots__ = ()
    _hx_class_name = "ValueType"
    _hx_constructs = ["TNull", "TInt", "TFloat", "TBool", "TObject", "TFunction", "TClass", "TEnum", "TUnknown"]

    @staticmethod
    def TClass(c):
        return ValueType("TClass", 6, (c,))

    @staticmethod
    def TEnum(e):
        return ValueType("TEnum", 7, (e,))
ValueType.TNull = ValueType("TNull", 0, ())
ValueType.TInt = ValueType("TInt", 1, ())
ValueType.TFloat = ValueType("TFloat", 2, ())
ValueType.TBool = ValueType("TBool", 3, ())
ValueType.TObject = ValueType("TObject", 4, ())
ValueType.TFunction = ValueType("TFunction", 5, ())
ValueType.TUnknown = ValueType("TUnknown", 8, ())
ValueType._hx_class = ValueType


class Type:
    _hx_class_name = "Type"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["getClass", "typeof"]

    @staticmethod
    def getClass(o):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Type.hx:44
        if (o is None):
            return None
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Type.hx:47
        o1 = o
        if ((o1 is not None) and ((HxOverrides.eq(o1,str) or python_lib_Inspect.isclass(o1)))):
            return None
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Type.hx:50
        if isinstance(o,_hx_AnonObject):
            return None
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Type.hx:53
        if hasattr(o,"_hx_class"):
            return o._hx_class
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Type.hx:56
        if hasattr(o,"__class__"):
            return o.__class__
        else:
            return None

    @staticmethod
    def typeof(v):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/Type.hx:180
        if (v is None):
            return ValueType.TNull
        elif isinstance(v,bool):
            return ValueType.TBool
        elif isinstance(v,int):
            return ValueType.TInt
        elif isinstance(v,float):
            return ValueType.TFloat
        elif isinstance(v,str):
            return ValueType.TClass(str)
        elif isinstance(v,list):
            return ValueType.TClass(list)
        elif (isinstance(v,_hx_AnonObject) or python_lib_Inspect.isclass(v)):
            return ValueType.TObject
        elif isinstance(v,Enum):
            return ValueType.TEnum(v.__class__)
        elif (isinstance(v,type) or hasattr(v,"_hx_class")):
            return ValueType.TClass(v.__class__)
        elif callable(v):
            return ValueType.TFunction
        else:
            return ValueType.TUnknown
Type._hx_class = Type


class a8_Constants:
    _hx_class_name = "a8.Constants"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["a8VersionsVersion"]
a8_Constants._hx_class = a8_Constants


class a8_DateOps:
    _hx_class_name = "a8.DateOps"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["midnight"]

    @staticmethod
    def midnight():
        # src/a8/DateOps.hx:7
        now = Date.now()
        # src/a8/DateOps.hx:8
        oneSecondBeforeMidnight = Date(now.date.year,(now.date.month - 1),now.date.day,23,59,59)
        # src/a8/DateOps.hx:9
        return Date.fromTime(((oneSecondBeforeMidnight.date.timestamp() * 1000) + 1000))
a8_DateOps._hx_class = a8_DateOps


class a8_Exception:
    _hx_class_name = "a8.Exception"
    _hx_is_interface = "False"
    __slots__ = ("message", "causedBy", "callStack", "posInfos")
    _hx_fields = ["message", "causedBy", "callStack", "posInfos"]
    _hx_methods = ["toString", "rethrow"]
    _hx_statics = ["thro"]

    def __init__(self,message,causedBy = None,posInfos = None):
        # src/a8/Exception.hx:19
        self.message = message
        # src/a8/Exception.hx:20
        self.causedBy = a8_OptionOps.toOption(causedBy)
        # src/a8/Exception.hx:21
        self.callStack = haxe__CallStack_CallStack_Impl_.callStack()
        # src/a8/Exception.hx:22
        self.posInfos = posInfos

    def toString(self):
        # src/a8/Exception.hx:26
        return ((((((HxOverrides.stringOrNull(self.posInfos.fileName) + ":") + Std.string(self.posInfos.lineNumber)) + " ") + HxOverrides.stringOrNull(self.message)) + "\n") + HxOverrides.stringOrNull(a8_HaxeOps2.asString(self.callStack,"    ")))

    def rethrow(self,context,posInfos = None):
        # src/a8/Exception.hx:35
        raise haxe_Exception.thrown(a8_Exception(context,self,posInfos))

    @staticmethod
    def thro(message):
        # src/a8/Exception.hx:10
        raise haxe_Exception.thrown(a8_Exception(message,None,_hx_AnonObject({'fileName': "src/a8/Exception.hx", 'lineNumber': 10, 'className': "a8.Exception", 'methodName': "thro"})))

a8_Exception._hx_class = a8_Exception


class a8_Exec:
    _hx_class_name = "a8.Exec"
    _hx_is_interface = "False"
    __slots__ = ("args", "cwd", "env", "failOnNonZeroExitCode", "executable")
    _hx_fields = ["args", "cwd", "env", "failOnNonZeroExitCode", "executable"]
    _hx_methods = ["asCommandLine", "execInline", "execCapture"]

    def __init__(self):
        # src/a8/Exec.hx:16
        self.failOnNonZeroExitCode = True
        # src/a8/Exec.hx:13
        self.args = []
        # src/a8/Exec.hx:14
        self.cwd = haxe_ds_Option._hx_None
        # src/a8/Exec.hx:15
        self.env = haxe_ds_Option._hx_None
        # src/a8/Exec.hx:17
        self.executable = haxe_ds_Option._hx_None

    def asCommandLine(self):
        # src/a8/Exec.hx:23
        _this = self.args
        return " ".join([python_Boot.toString1(x1,'') for x1 in _this])

    def execInline(self):
        # src/a8/Exec.hx:31
        a8_Logger.trace(("running -- " + HxOverrides.stringOrNull(self.asCommandLine())),_hx_AnonObject({'fileName': "src/a8/Exec.hx", 'lineNumber': 31, 'className': "a8.Exec", 'methodName': "execInline"}))
        # src/a8/Exec.hx:32
        exitCode = python_lib_Subprocess.call(self.args,**python__KwArgs_KwArgs_Impl_.fromT(_hx_AnonObject({'cwd': a8_OptionOps.getOrElse(self.cwd,None)})))
        # src/a8/Exec.hx:39
        if ((exitCode != 0) and self.failOnNonZeroExitCode):
            a8_Exception.thro(((("non-zero exit code of " + Std.string(exitCode)) + " while executing -- ") + HxOverrides.stringOrNull(self.asCommandLine())))
        # src/a8/Exec.hx:42
        return exitCode

    def execCapture(self):
        # src/a8/Exec.hx:49
        a8_Logger.trace(("running -- " + HxOverrides.stringOrNull(self.asCommandLine())),_hx_AnonObject({'fileName': "src/a8/Exec.hx", 'lineNumber': 49, 'className': "a8.Exec", 'methodName': "execCapture"}))
        # src/a8/Exec.hx:52
        popen = self.args
        # src/a8/Exec.hx:54
        popen1 = a8_OptionOps.getOrElse(self.executable,(self.args[0] if 0 < len(self.args) else None))
        # src/a8/Exec.hx:56
        popen2 = python_lib_Subprocess.PIPE
        # src/a8/Exec.hx:57
        popen3 = python_lib_Subprocess.PIPE
        # src/a8/Exec.hx:61
        popen4 = a8_OptionOps.getOrElse(self.cwd,None)
        # src/a8/Exec.hx:62
        o = self.env
        popen5 = None
        if (o.index == 0):
            v = o.params[0]
            popen5 = haxe_ds_Option.Some(a8_PyOps.toDict(v))
        else:
            popen5 = haxe_ds_Option._hx_None
        # src/a8/Exec.hx:50
        popen6 = python_lib_subprocess_Popen(popen,None,popen1,None,popen2,popen3,None,False,False,popen4,a8_OptionOps.getOrElse(popen5,None))
        # src/a8/Exec.hx:65
        def _hx_local_0(out):
            pass
        firstIO = _hx_local_0
        # src/a8/Exec.hx:68
        timestampStr = a8_PathOps.timestampStr()
        # src/a8/Exec.hx:70
        stdoutCapture = haxe_io_BytesOutput()
        # src/a8/Exec.hx:71
        stderrCapture = haxe_io_BytesOutput()
        # src/a8/Exec.hx:73
        pipedStdout = a8_Pipe(a8_StreamOps.asInputStream(popen6.stdout),a8_StreamOps2.asOutputStream(stdoutCapture),firstIO)
        # src/a8/Exec.hx:74
        pipedStderr = a8_Pipe(a8_StreamOps.asInputStream(popen6.stderr),a8_StreamOps2.asOutputStream(stderrCapture),firstIO)
        # src/a8/Exec.hx:76
        pipedStdout.run()
        # src/a8/Exec.hx:77
        pipedStderr.run()
        # src/a8/Exec.hx:79
        popen6.wait()
        # src/a8/Exec.hx:81
        result = _hx_AnonObject({'exitCode': popen6.returncode, 'stderr': a8_HaxeOps.asString(stderrCapture.getBytes()), 'stdout': a8_HaxeOps.asString(stdoutCapture.getBytes())})
        # src/a8/Exec.hx:88
        a8_Logger.trace(("" + Std.string(result.exitCode)),_hx_AnonObject({'fileName': "src/a8/Exec.hx", 'lineNumber': 88, 'className': "a8.Exec", 'methodName': "execCapture"}))
        # src/a8/Exec.hx:89
        if ((result.exitCode != 0) and self.failOnNonZeroExitCode):
            a8_Exception.thro(((("non-zero exit code of " + Std.string(result.exitCode)) + " while executing -- ") + HxOverrides.stringOrNull(self.asCommandLine())))
        # src/a8/Exec.hx:93
        return result

a8_Exec._hx_class = a8_Exec


class a8_PyOps:
    _hx_class_name = "a8.PyOps"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["toDict", "spawn"]

    @staticmethod
    def toDict(_hx_map):
        # src/a8/PyOps.hx:53
        _hx_dict = dict()
        # src/a8/PyOps.hx:54
        # src/a8/PyOps.hx:54
        k = _hx_map.keys()
        while k.hasNext():
            k1 = k.next()
            # src/a8/PyOps.hx:55
            _hx_dict[k1] = _hx_map.get(k1)
        # src/a8/PyOps.hx:57
        return _hx_dict

    @staticmethod
    def spawn(fn):
        # src/a8/PyOps.hx:62
        th = python_lib_threading_Thread(**python__KwArgs_KwArgs_Impl_.fromT(_hx_AnonObject({'target': fn})))
        # src/a8/PyOps.hx:63
        th.daemon = True
        # src/a8/PyOps.hx:64
        th.start()
        # src/a8/PyOps.hx:66
        return th
a8_PyOps._hx_class = a8_PyOps


class python__KwArgs_KwArgs_Impl_:
    _hx_class_name = "python._KwArgs.KwArgs_Impl_"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["fromT"]

    @staticmethod
    def fromT(d):
        # /Users/glen/bin/haxe-4.2.5/std/python/KwArgs.hx:59
        this1 = python_Lib.anonAsDict(d)
        return this1
python__KwArgs_KwArgs_Impl_._hx_class = python__KwArgs_KwArgs_Impl_


class python_Lib:
    _hx_class_name = "python.Lib"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["lineEnd", "printString", "dictToAnon", "anonToDict", "anonAsDict"]

    @staticmethod
    def printString(_hx_str):
        # /Users/glen/bin/haxe-4.2.5/std/python/Lib.hx:51
        encoding = "utf-8"
        if (encoding is None):
            encoding = "utf-8"
        python_lib_Sys.stdout.buffer.write(_hx_str.encode(encoding, "strict"))
        # /Users/glen/bin/haxe-4.2.5/std/python/Lib.hx:52
        python_lib_Sys.stdout.flush()

    @staticmethod
    def dictToAnon(v):
        # /Users/glen/bin/haxe-4.2.5/std/python/Lib.hx:67
        return _hx_AnonObject(v.copy())

    @staticmethod
    def anonToDict(o):
        # /Users/glen/bin/haxe-4.2.5/std/python/Lib.hx:75
        if isinstance(o,_hx_AnonObject):
            return o.__dict__.copy()
        else:
            return None

    @staticmethod
    def anonAsDict(o):
        # /Users/glen/bin/haxe-4.2.5/std/python/Lib.hx:86
        if isinstance(o,_hx_AnonObject):
            return o.__dict__
        else:
            return None
python_Lib._hx_class = python_Lib


class a8_GlobalScheduler:
    _hx_class_name = "a8.GlobalScheduler"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["scheduler", "schedule", "submit"]

    @staticmethod
    def schedule(delayInSeconds,fn):
        # src/a8/GlobalScheduler.hx:22
        a8_GlobalScheduler.scheduler.enter(delayInSeconds,1.0,fn)

    @staticmethod
    def submit(fn):
        # src/a8/GlobalScheduler.hx:26
        a8_GlobalScheduler.schedule(0,fn)
a8_GlobalScheduler._hx_class = a8_GlobalScheduler


class a8_HaxeOps:
    _hx_class_name = "a8.HaxeOps"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["asString", "toMap", "isDigit", "isAlpha", "isWhitespace", "isHaxeIdentifierFirstChar", "isHaxeIdentifierSecondChar"]

    @staticmethod
    def asString(_hx_bytes):
        # src/a8/HaxeOps.hx:12
        return _hx_bytes.getString(0,_hx_bytes.length)

    @staticmethod
    def toMap(iterable,keyFn):
        # src/a8/HaxeOps.hx:16
        _hx_map = haxe_ds_StringMap()
        # src/a8/HaxeOps.hx:17
        def _hx_local_0(a):
            # src/a8/HaxeOps.hx:17
            key = keyFn(a)
            _hx_map.h[key] = a
        Lambda.iter(iterable,_hx_local_0)
        # src/a8/HaxeOps.hx:18
        return _hx_map

    @staticmethod
    def isDigit(ch):
        # src/a8/HaxeOps.hx:23
        if ((len(ch) == 1) and ((ch >= "0"))):
            return (ch <= "0")
        else:
            return False

    @staticmethod
    def isAlpha(ch):
        # src/a8/HaxeOps.hx:29
        if (len(ch) == 1):
            if (not (((ch >= "A") and ((ch <= "Z"))))):
                if (ch >= "a"):
                    return (ch <= "z")
                else:
                    return False
            else:
                return True
        else:
            return False

    @staticmethod
    def isWhitespace(ch):
        # src/a8/HaxeOps.hx:37
        ch1 = ch
        # src/a8/HaxeOps.hx:39
        if ((((ch1 == " ") or ((ch1 == "\r"))) or ((ch1 == "\n"))) or ((ch1 == "\t"))):
            return True
        else:
            return False

    @staticmethod
    def isHaxeIdentifierFirstChar(ch):
        # src/a8/HaxeOps.hx:47
        if (len(ch) == 1):
            if (not a8_HaxeOps.isAlpha(ch)):
                return (ch == "_")
            else:
                return True
        else:
            return False

    @staticmethod
    def isHaxeIdentifierSecondChar(ch):
        # src/a8/HaxeOps.hx:56
        if (not a8_HaxeOps.isHaxeIdentifierFirstChar(ch)):
            return a8_HaxeOps.isDigit(ch)
        else:
            return True
a8_HaxeOps._hx_class = a8_HaxeOps


class a8_HaxeOps2:
    _hx_class_name = "a8.HaxeOps2"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["asString", "toMap"]

    @staticmethod
    def asString(stack,indent = None):
        # src/a8/HaxeOps.hx:67
        if (indent is None):
            indent = ""
        # src/a8/HaxeOps.hx:71
        def _hx_local_0(si):
            # src/a8/HaxeOps.hx:71
            return (("null" if indent is None else indent) + Std.string(si))
        # src/a8/HaxeOps.hx:70
        _this = list(map(_hx_local_0,stack))
        s = "\n".join([python_Boot.toString1(x1,'') for x1 in _this])
        # src/a8/HaxeOps.hx:73
        return s

    @staticmethod
    def toMap(iterable):
        # src/a8/HaxeOps.hx:77
        _hx_map = haxe_ds_StringMap()
        # src/a8/HaxeOps.hx:78
        # src/a8/HaxeOps.hx:78
        t = HxOverrides.iterator(iterable)
        while t.hasNext():
            t1 = t.next()
            # src/a8/HaxeOps.hx:79
            _hx_map.h[python_internal_ArrayImpl._get(t1, 0)] = python_internal_ArrayImpl._get(t1, 1)
        # src/a8/HaxeOps.hx:81
        return _hx_map
a8_HaxeOps2._hx_class = a8_HaxeOps2


class a8_Logger:
    _hx_class_name = "a8.Logger"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["traceEnabled", "trace", "warn"]

    @staticmethod
    def trace(msg,posInfo = None):
        # src/a8/Logger.hx:12
        if a8_Logger.traceEnabled:
            haxe_Log.trace(("TRACE - " + ("null" if msg is None else msg)),posInfo)

    @staticmethod
    def warn(msg,posInfo = None):
        # src/a8/Logger.hx:18
        haxe_Log.trace(("WARN - " + ("null" if msg is None else msg)),posInfo)
a8_Logger._hx_class = a8_Logger


class a8_OptionOps:
    _hx_class_name = "a8.OptionOps"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["toOption", "nonEmpty", "isEmpty", "getOrError", "getOrElse", "getOrElseFn", "get", "iter"]

    @staticmethod
    def toOption(a):
        # src/a8/OptionOps.hx:14
        if (a is None):
            return haxe_ds_Option._hx_None
        else:
            return haxe_ds_Option.Some(a)

    @staticmethod
    def nonEmpty(o):
        # src/a8/OptionOps.hx:20
        tmp = o.index
        # src/a8/OptionOps.hx:21
        if (tmp == 0):
            # src/a8/OptionOps.hx:21
            _g = o.params[0]
            return True
        elif (tmp == 1):
            return False
        else:
            pass

    @staticmethod
    def isEmpty(o):
        # src/a8/OptionOps.hx:27
        return (not a8_OptionOps.nonEmpty(o))

    @staticmethod
    def getOrError(o,msg):
        # src/a8/OptionOps.hx:33
        tmp = o.index
        # src/a8/OptionOps.hx:34
        if (tmp == 0):
            # src/a8/OptionOps.hx:34
            i = o.params[0]
            return i
        elif (tmp == 1):
            raise haxe_Exception.thrown(a8_Exception(msg,None,_hx_AnonObject({'fileName': "src/a8/OptionOps.hx", 'lineNumber': 35, 'className': "a8.OptionOps", 'methodName': "getOrError"})))
        else:
            pass

    @staticmethod
    def getOrElse(o,_hx_def):
        # src/a8/OptionOps.hx:41
        tmp = o.index
        # src/a8/OptionOps.hx:42
        if (tmp == 0):
            # src/a8/OptionOps.hx:42
            i = o.params[0]
            return i
        elif (tmp == 1):
            return _hx_def
        else:
            pass

    @staticmethod
    def getOrElseFn(o,_hx_def):
        # src/a8/OptionOps.hx:49
        tmp = o.index
        # src/a8/OptionOps.hx:50
        if (tmp == 0):
            # src/a8/OptionOps.hx:50
            i = o.params[0]
            return i
        elif (tmp == 1):
            return _hx_def()
        else:
            pass

    @staticmethod
    def get(o):
        # src/a8/OptionOps.hx:56
        return a8_OptionOps.getOrError(o,"expected a Some")

    @staticmethod
    def iter(o,fn):
        # src/a8/OptionOps.hx:61
        tmp = o.index
        # src/a8/OptionOps.hx:62
        if (tmp == 0):
            # src/a8/OptionOps.hx:62
            a = o.params[0]
            fn(a)
        elif (tmp == 1):
            pass
        else:
            pass
a8_OptionOps._hx_class = a8_OptionOps


class a8_PathOps:
    _hx_class_name = "a8.PathOps"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["timestampStr", "path", "symlinkChain", "executablePath", "userHome", "absPath", "name", "programPath", "readText", "readLines", "makeDirectories", "readBytes", "exists", "isAbsolute", "files", "basename", "moveTo", "deleteFile", "entries", "isFile", "isDir", "realPathStr", "writeBytes", "writeText", "parent", "entry", "outputStream", "readProperties"]

    @staticmethod
    def timestampStr():
        # src/a8/PathOps.hx:14
        now = Date.now()
        # src/a8/PathOps.hx:16
        def _hx_local_0(i):
            # src/a8/PathOps.hx:16
            return StringTools.lpad(("" + Std.string(i)),"0",2)
        # src/a8/PathOps.hx:15
        pad = _hx_local_0
        # src/a8/PathOps.hx:18
        return ((((((Std.string(now.date.year) + HxOverrides.stringOrNull(pad((now.date.month - 1)))) + HxOverrides.stringOrNull(pad(now.date.day))) + "_") + HxOverrides.stringOrNull(pad(now.date.hour))) + HxOverrides.stringOrNull(pad(now.date.minute))) + HxOverrides.stringOrNull(pad(now.date.second)))

    @staticmethod
    def path(p):
        # src/a8/PathOps.hx:22
        return haxe_io_Path(p)

    @staticmethod
    def symlinkChain(p):
        # src/a8/PathOps.hx:26
        paths = []
        # src/a8/PathOps.hx:27
        impl = None
        def _hx_local_0(thePath):
            # src/a8/PathOps.hx:28
            # src/a8/PathOps.hx:28
            x = a8_PathOps.absPath(thePath)
            paths.append(x)
            # src/a8/PathOps.hx:29
            if python_lib_os_Path.islink(thePath.toString()):
                # src/a8/PathOps.hx:30
                relativeLink = a8_PyOs2.readlink(thePath.toString())
                # src/a8/PathOps.hx:31
                absoluteLink = (relativeLink if (python_lib_os_Path.isabs(relativeLink)) else python_lib_os_Path.join(a8_PathOps.parent(thePath).toString(),relativeLink))
                # src/a8/PathOps.hx:36
                p = a8_PathOps.path(absoluteLink)
                # src/a8/PathOps.hx:37
                impl(p)
        impl = _hx_local_0
        # src/a8/PathOps.hx:40
        impl(p)
        # src/a8/PathOps.hx:41
        return paths

    @staticmethod
    def executablePath():
        # src/a8/PathOps.hx:49
        return a8_PlatformOps.instance.executablePath()

    @staticmethod
    def userHome():
        # src/a8/PathOps.hx:53
        return haxe_io_Path(Sys.environment().h.get("HOME",None))

    @staticmethod
    def absPath(p):
        # src/a8/PathOps.hx:57
        return a8_PlatformOps.instance.absPath(p)

    @staticmethod
    def name(p):
        # src/a8/PathOps.hx:62
        if (p.ext is None):
            return p.file
        else:
            return ((HxOverrides.stringOrNull(p.file) + ".") + HxOverrides.stringOrNull(p.ext))

    @staticmethod
    def programPath():
        # src/a8/PathOps.hx:74
        return haxe_io_Path(Sys.programPath())

    @staticmethod
    def readText(path):
        # src/a8/PathOps.hx:78
        return sys_io_File.getContent(path.toString())

    @staticmethod
    def readLines(path):
        # src/a8/PathOps.hx:82
        _this = a8_PathOps.readText(path)
        return _this.split("\n")

    @staticmethod
    def makeDirectories(path):
        # src/a8/PathOps.hx:86
        sys_FileSystem.createDirectory(path.toString())

    @staticmethod
    def readBytes(path):
        # src/a8/PathOps.hx:90
        return sys_io_File.getBytes(path.toString())

    @staticmethod
    def exists(path):
        # src/a8/PathOps.hx:94
        return sys_FileSystem.exists(path.toString())

    @staticmethod
    def isAbsolute(path):
        # src/a8/PathOps.hx:98
        return haxe_io_Path.isAbsolute(path.toString())

    @staticmethod
    def files(parentDir):
        # src/a8/PathOps.hx:103
        def _hx_local_1():
            # src/a8/PathOps.hx:105
            def _hx_local_0(e):
                # src/a8/PathOps.hx:105
                return a8_PathOps.isFile(e)
            # src/a8/PathOps.hx:103
            return list(filter(_hx_local_0,a8_PathOps.entries(parentDir)))
        return _hx_local_1()

    @staticmethod
    def basename(path):
        # src/a8/PathOps.hx:113
        suffix = ("" if ((path.ext is None)) else ("." + HxOverrides.stringOrNull(path.ext)))
        # src/a8/PathOps.hx:114
        return (HxOverrides.stringOrNull(path.file) + ("null" if suffix is None else suffix))

    @staticmethod
    def moveTo(source,target):
        # src/a8/PathOps.hx:118
        a8_PlatformOps.instance.moveTo(source,target)

    @staticmethod
    def deleteFile(source):
        # src/a8/PathOps.hx:122
        if a8_PathOps.exists(source):
            sys_FileSystem.deleteFile(source.toString())

    @staticmethod
    def entries(parentDir):
        # src/a8/PathOps.hx:128
        sep = ("" if (parentDir.backslash) else "/")
        # src/a8/PathOps.hx:130
        if a8_PathOps.exists(parentDir):
            # src/a8/PathOps.hx:131
            def _hx_local_1():
                # src/a8/PathOps.hx:134
                def _hx_local_0(e):
                    # src/a8/PathOps.hx:134
                    return haxe_io_Path(((HxOverrides.stringOrNull(parentDir.toString()) + ("null" if sep is None else sep)) + ("null" if e is None else e)))
                # src/a8/PathOps.hx:131
                return list(map(_hx_local_0,sys_FileSystem.readDirectory(a8_PathOps.realPathStr(parentDir))))
            return _hx_local_1()
        else:
            return []

    @staticmethod
    def isFile(path):
        # src/a8/PathOps.hx:141
        return a8_PlatformOps.instance.isFile(path)

    @staticmethod
    def isDir(path):
        # src/a8/PathOps.hx:145
        return sys_FileSystem.isDirectory(path.toString())

    @staticmethod
    def realPathStr(path):
        # src/a8/PathOps.hx:149
        return sys_FileSystem.fullPath(path.toString())

    @staticmethod
    def writeBytes(path,_hx_bytes):
        # src/a8/PathOps.hx:153
        sys_io_File.saveBytes(path.toString(),_hx_bytes)

    @staticmethod
    def writeText(path,text):
        # src/a8/PathOps.hx:157
        sys_io_File.saveContent(path.toString(),text)

    @staticmethod
    def parent(path):
        # src/a8/PathOps.hx:161
        _g = path.dir
        # src/a8/PathOps.hx:162
        if (_g is None):
            if a8_PathOps.isAbsolute(path):
                return None
            else:
                return haxe_io_Path(sys_FileSystem.fullPath("."))
        else:
            # src/a8/PathOps.hx:168
            d = _g
            # src/a8/PathOps.hx:169
            return haxe_io_Path(d)

    @staticmethod
    def entry(dir,name):
        # src/a8/PathOps.hx:174
        separator = ("" if (dir.backslash) else "/")
        # src/a8/PathOps.hx:175
        return haxe_io_Path(((HxOverrides.stringOrNull(dir.toString()) + ("null" if separator is None else separator)) + ("null" if name is None else name)))

    @staticmethod
    def outputStream(p):
        # src/a8/PathOps.hx:179
        return a8_StreamOps.fileOutputStream(a8_PathOps.realPathStr(p))

    @staticmethod
    def readProperties(p,failOnNotFound = None):
        # src/a8/PathOps.hx:183
        rf = a8_OptionOps.getOrElse(a8_OptionOps.toOption(failOnNotFound),False)
        # src/a8/PathOps.hx:184
        exists = a8_PathOps.exists(p)
        # src/a8/PathOps.hx:186
        if ((not exists) and (not rf)):
            return haxe_ds_StringMap()
        else:
            # src/a8/PathOps.hx:189
            _g = []
            x = HxOverrides.iterator(a8_PathOps.readLines(p))
            while x.hasNext():
                x1 = x.next()
                # src/a8/PathOps.hx:191
                a = x1.split("=")
                # src/a8/PathOps.hx:189
                x2 = None
                # src/a8/PathOps.hx:193
                if (len(a) == 2):
                    # src/a8/PathOps.hx:194
                    this1 = [(a[0] if 0 < len(a) else None), (a[1] if 1 < len(a) else None)]
                    # src/a8/PathOps.hx:189
                    x2 = [this1]
                else:
                    x2 = []
                # src/a8/PathOps.hx:189
                _g.append(x2)
            _g1 = []
            e = HxOverrides.iterator(_g)
            while e.hasNext():
                e1 = e.next()
                x = HxOverrides.iterator(e1)
                while x.hasNext():
                    x1 = x.next()
                    _g1.append(x1)
            return a8_HaxeOps2.toMap(_g1)
a8_PathOps._hx_class = a8_PathOps


class a8_AbstractPlatform:
    _hx_class_name = "a8.AbstractPlatform"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_methods = ["isFile", "spawn", "moveTo"]

    def isFile(self,path):
        # src/a8/Platform.hx:42
        e = sys_FileSystem.exists(path.toString())
        # src/a8/Platform.hx:43
        d = sys_FileSystem.isDirectory(path.toString())
        # src/a8/Platform.hx:44
        if e:
            return (not d)
        else:
            return False

    def spawn(self,threadName,fn):
        # src/a8/Platform.hx:48
        raise haxe_Exception.thrown(a8_Exception("TODO ??? implement me",None,_hx_AnonObject({'fileName': "src/a8/Platform.hx", 'lineNumber': 48, 'className': "a8.AbstractPlatform", 'methodName': "spawn"})))

    def moveTo(self,source,target):
        # src/a8/Platform.hx:52
        raise haxe_Exception.thrown(a8_Exception("TODO ??? implement me",None,_hx_AnonObject({'fileName': "src/a8/Platform.hx", 'lineNumber': 52, 'className': "a8.AbstractPlatform", 'methodName': "moveTo"})))

a8_AbstractPlatform._hx_class = a8_AbstractPlatform


class a8_Platform:
    _hx_class_name = "a8.Platform"
    _hx_is_interface = "True"
    __slots__ = ()
    _hx_methods = ["executablePath", "isFile", "spawn", "moveTo", "absPath"]
a8_Platform._hx_class = a8_Platform


class a8_PythonPlatform(a8_AbstractPlatform):
    _hx_class_name = "a8.PythonPlatform"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = ["absPath", "executablePath", "isFile", "spawn", "moveTo"]
    _hx_statics = []
    _hx_interfaces = [a8_Platform]
    _hx_super = a8_AbstractPlatform


    def __init__(self):
        pass

    def absPath(self,path):
        # src/a8/Platform.hx:77
        return a8_PathOps.path(python_lib_os_Path.normpath(python_lib_os_Path.abspath(path.toString())))

    def executablePath(self):
        # src/a8/Platform.hx:81
        return haxe_io_Path(python_internal_ArrayImpl._get(python_lib_Sys.argv, 0))

    def isFile(self,path):
        # src/a8/Platform.hx:85
        return python_lib_os_Path.isfile(path.toString())

    def spawn(self,threadName,fn):
        # src/a8/Platform.hx:89
        th = python_lib_threading_Thread(**python__KwArgs_KwArgs_Impl_.fromT(_hx_AnonObject({'target': fn})))
        # src/a8/Platform.hx:90
        th.start()

    def moveTo(self,source,target):
        # src/a8/Platform.hx:94
        a8_PyShutil2.move(source.toString(),target.toString())

a8_PythonPlatform._hx_class = a8_PythonPlatform


class a8_PlatformOps:
    _hx_class_name = "a8.PlatformOps"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["instance"]
a8_PlatformOps._hx_class = a8_PlatformOps


class a8_StreamOps:
    _hx_class_name = "a8.StreamOps"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["asInputStream", "asOutputStream", "fileOutputStream"]

    @staticmethod
    def asInputStream(fileIO):
        # src/a8/StreamOps.hx:12
        return a8_FileIOInputStream(fileIO)

    @staticmethod
    def asOutputStream(io):
        # src/a8/StreamOps.hx:16
        return a8_TextIOBaseOutputStream(io)

    @staticmethod
    def fileOutputStream(filename):
        # src/a8/StreamOps.hx:20
        return a8_StreamOps.asOutputStream(python_lib_Io.open(filename,"wt"))
a8_StreamOps._hx_class = a8_StreamOps


class a8_StreamOps2:
    _hx_class_name = "a8.StreamOps2"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["asOutputStream"]

    @staticmethod
    def asOutputStream(output):
        # src/a8/StreamOps.hx:28
        return a8_OutputOutputStream(output)
a8_StreamOps2._hx_class = a8_StreamOps2


class a8_OutputStream:
    _hx_class_name = "a8.OutputStream"
    _hx_is_interface = "True"
    __slots__ = ()
    _hx_methods = ["write", "flush", "close"]
a8_OutputStream._hx_class = a8_OutputStream


class a8_InputStream:
    _hx_class_name = "a8.InputStream"
    _hx_is_interface = "True"
    __slots__ = ()
    _hx_methods = ["readLine", "close"]
a8_InputStream._hx_class = a8_InputStream


class a8_FileIOInputStream:
    _hx_class_name = "a8.FileIOInputStream"
    _hx_is_interface = "False"
    __slots__ = ("delegate",)
    _hx_fields = ["delegate"]
    _hx_methods = ["readLine", "close"]
    _hx_interfaces = [a8_InputStream]

    def __init__(self,delegate):
        # src/a8/Streams.hx:29
        self.delegate = delegate

    def readLine(self):
        # src/a8/Streams.hx:32
        _hx_bytes = self.delegate.readline()
        # src/a8/Streams.hx:33
        line = _hx_bytes.decode()
        # src/a8/Streams.hx:36
        if line.endswith("\n"):
            return HxString.substr(line,0,(len(line) - 1))
        else:
            return None

    def close(self):
        pass

a8_FileIOInputStream._hx_class = a8_FileIOInputStream


class a8_TextIOBaseOutputStream:
    _hx_class_name = "a8.TextIOBaseOutputStream"
    _hx_is_interface = "False"
    __slots__ = ("delegate",)
    _hx_fields = ["delegate"]
    _hx_methods = ["write", "flush", "close"]
    _hx_interfaces = [a8_OutputStream]

    def __init__(self,delegate):
        # src/a8/Streams.hx:53
        self.delegate = delegate

    def write(self,s):
        # src/a8/Streams.hx:56
        self.delegate.write(s)

    def flush(self):
        # src/a8/Streams.hx:60
        self.delegate.flush()

    def close(self):
        # src/a8/Streams.hx:64
        self.delegate.close()

a8_TextIOBaseOutputStream._hx_class = a8_TextIOBaseOutputStream


class a8_OutputOutputStream:
    _hx_class_name = "a8.OutputOutputStream"
    _hx_is_interface = "False"
    __slots__ = ("delegate",)
    _hx_fields = ["delegate"]
    _hx_methods = ["write", "flush", "close"]
    _hx_interfaces = [a8_OutputStream]

    def __init__(self,delegate):
        # src/a8/Streams.hx:73
        self.delegate = delegate

    def write(self,s):
        # src/a8/Streams.hx:76
        self.delegate.writeString(s)

    def flush(self):
        # src/a8/Streams.hx:80
        self.delegate.flush()

    def close(self):
        # src/a8/Streams.hx:84
        self.delegate.close()

a8_OutputOutputStream._hx_class = a8_OutputOutputStream


class a8_FileIOOutputStream:
    _hx_class_name = "a8.FileIOOutputStream"
    _hx_is_interface = "False"
    __slots__ = ("delegate",)
    _hx_fields = ["delegate"]
    _hx_methods = ["write", "flush", "close"]
    _hx_interfaces = [a8_OutputStream]

    def __init__(self,delegate):
        # src/a8/Streams.hx:92
        self.delegate = delegate

    def write(self,s):
        # src/a8/Streams.hx:95
        self.delegate.write(bytes(s,"utf-8"))

    def flush(self):
        # src/a8/Streams.hx:99
        self.delegate.flush()

    def close(self):
        # src/a8/Streams.hx:103
        self.delegate.close()

a8_FileIOOutputStream._hx_class = a8_FileIOOutputStream


class a8_TeeOutputStream:
    _hx_class_name = "a8.TeeOutputStream"
    _hx_is_interface = "False"
    __slots__ = ("outputs",)
    _hx_fields = ["outputs"]
    _hx_methods = ["write", "flush", "close"]
    _hx_interfaces = [a8_OutputStream]

    def __init__(self,outputs):
        # src/a8/Streams.hx:115
        self.outputs = outputs

    def write(self,s):
        # src/a8/Streams.hx:120
        def _hx_local_0(os):
            # src/a8/Streams.hx:120
            os.write(s)
        # src/a8/Streams.hx:119
        Lambda.iter(self.outputs,_hx_local_0)

    def flush(self):
        # src/a8/Streams.hx:126
        def _hx_local_0(os):
            # src/a8/Streams.hx:126
            os.flush()
        # src/a8/Streams.hx:125
        Lambda.iter(self.outputs,_hx_local_0)

    def close(self):
        # src/a8/Streams.hx:132
        def _hx_local_0(os):
            # src/a8/Streams.hx:132
            os.close()
        # src/a8/Streams.hx:131
        Lambda.iter(self.outputs,_hx_local_0)

a8_TeeOutputStream._hx_class = a8_TeeOutputStream


class a8_Pipe:
    _hx_class_name = "a8.Pipe"
    _hx_is_interface = "False"
    __slots__ = ("input", "output", "firstIO", "byteCount", "replaceOutput")
    _hx_fields = ["input", "output", "firstIO", "byteCount", "replaceOutput"]
    _hx_methods = ["run"]

    def __init__(self,input,output,firstIO):
        # src/a8/Streams.hx:148
        self.replaceOutput = None
        # src/a8/Streams.hx:151
        self.input = input
        # src/a8/Streams.hx:152
        self.output = output
        # src/a8/Streams.hx:153
        self.firstIO = firstIO
        # src/a8/Streams.hx:154
        self.byteCount = 0

    def run(self):
        # src/a8/Streams.hx:160
        _gthis = self
        # src/a8/Streams.hx:162
        def _hx_local_1():
            # src/a8/Streams.hx:163
            first = True
            # src/a8/Streams.hx:164
            cont = True
            # src/a8/Streams.hx:165
            while cont:
                # src/a8/Streams.hx:166
                line = _gthis.input.readLine()
                # src/a8/Streams.hx:167
                if (_gthis.replaceOutput is not None):
                    # src/a8/Streams.hx:168
                    _gthis.output = _gthis.replaceOutput(_gthis.output)
                    # src/a8/Streams.hx:169
                    first = True
                # src/a8/Streams.hx:171
                if (line is None):
                    cont = False
                else:
                    # src/a8/Streams.hx:174
                    if first:
                        # src/a8/Streams.hx:175
                        _gthis.firstIO(_gthis.output)
                        # src/a8/Streams.hx:176
                        first = False
                    # src/a8/Streams.hx:178
                    _gthis.output.write(line)
                    # src/a8/Streams.hx:179
                    _gthis.output.write("\n")
                    # src/a8/Streams.hx:180
                    _gthis.output.flush()
                    # src/a8/Streams.hx:181
                    _gthis.byteCount = (_gthis.byteCount + ((len(line) + 1)))
            # src/a8/Streams.hx:184
            _gthis.output.close()
        impl = _hx_local_1
        # src/a8/Streams.hx:187
        a8_PlatformOps.instance.spawn("pipe",impl)

a8_Pipe._hx_class = a8_Pipe


class a8__Tuple2_Tuple2_Impl_:
    _hx_class_name = "a8._Tuple2.Tuple2_Impl_"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["_new", "_1", "_2", "toString"]

    @staticmethod
    def _new(a,b):
        # src/a8/Tuple2.hx:6
        this1 = [a, b]
        return this1

    @staticmethod
    def _1(this1):
        # src/a8/Tuple2.hx:11
        return (this1[0] if 0 < len(this1) else None)

    @staticmethod
    def _2(this1):
        # src/a8/Tuple2.hx:15
        return (this1[1] if 1 < len(this1) else None)

    @staticmethod
    def toString(this1):
        # src/a8/Tuple2.hx:19
        return haxe_format_JsonPrinter.print(this1,None,None)
a8__Tuple2_Tuple2_Impl_._hx_class = a8__Tuple2_Tuple2_Impl_

class haxe_ds_Option(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.ds.Option"
    _hx_constructs = ["Some", "None"]

    @staticmethod
    def Some(v):
        return haxe_ds_Option("Some", 0, (v,))
haxe_ds_Option._hx_None = haxe_ds_Option("None", 1, ())
haxe_ds_Option._hx_class = haxe_ds_Option


class haxe_IMap:
    _hx_class_name = "haxe.IMap"
    _hx_is_interface = "True"
    __slots__ = ()
    _hx_methods = ["get", "keys"]
haxe_IMap._hx_class = haxe_IMap


class haxe_ds_StringMap:
    _hx_class_name = "haxe.ds.StringMap"
    _hx_is_interface = "False"
    __slots__ = ("h",)
    _hx_fields = ["h"]
    _hx_methods = ["get", "keys"]
    _hx_interfaces = [haxe_IMap]

    def __init__(self):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/haxe/ds/StringMap.hx:32
        self.h = dict()

    def get(self,key):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/haxe/ds/StringMap.hx:40
        return self.h.get(key,None)

    def keys(self):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/haxe/ds/StringMap.hx:55
        return python_HaxeIterator(iter(self.h.keys()))

haxe_ds_StringMap._hx_class = haxe_ds_StringMap


class sys_io_File:
    _hx_class_name = "sys.io.File"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["getContent", "saveContent", "getBytes", "saveBytes"]

    @staticmethod
    def getContent(path):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/io/File.hx:31
        f = python_lib_Builtins.open(path,"r",-1,"utf-8",None,"")
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/io/File.hx:32
        content = f.read(-1)
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/io/File.hx:33
        f.close()
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/io/File.hx:34
        return content

    @staticmethod
    def saveContent(path,content):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/io/File.hx:38
        f = python_lib_Builtins.open(path,"w",-1,"utf-8",None,"")
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/io/File.hx:39
        f.write(content)
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/io/File.hx:40
        f.close()

    @staticmethod
    def getBytes(path):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/io/File.hx:44
        f = python_lib_Builtins.open(path,"rb",-1)
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/io/File.hx:45
        size = f.read(-1)
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/io/File.hx:46
        b = haxe_io_Bytes.ofData(size)
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/io/File.hx:47
        f.close()
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/io/File.hx:48
        return b

    @staticmethod
    def saveBytes(path,_hx_bytes):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/io/File.hx:52
        f = python_lib_Builtins.open(path,"wb",-1)
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/io/File.hx:53
        f.write(_hx_bytes.b)
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/io/File.hx:54
        f.close()
sys_io_File._hx_class = sys_io_File


class haxe_io_Path:
    _hx_class_name = "haxe.io.Path"
    _hx_is_interface = "False"
    __slots__ = ("dir", "file", "ext", "backslash")
    _hx_fields = ["dir", "file", "ext", "backslash"]
    _hx_methods = ["toString"]
    _hx_statics = ["isAbsolute"]

    def __init__(self,path):
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Path.hx:68
        self.backslash = None
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Path.hx:63
        self.ext = None
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Path.hx:53
        self.file = None
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Path.hx:43
        self.dir = None
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Path.hx:77
        path1 = path
        _hx_local_0 = len(path1)
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Path.hx:78
        if (_hx_local_0 == 1):
            if (path1 == "."):
                # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Path.hx:79
                self.dir = path
                # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Path.hx:80
                self.file = ""
                # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Path.hx:81
                return
        elif (_hx_local_0 == 2):
            if (path1 == ".."):
                # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Path.hx:79
                self.dir = path
                # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Path.hx:80
                self.file = ""
                # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Path.hx:81
                return
        else:
            pass
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Path.hx:83
        startIndex = None
        c1 = None
        if (startIndex is None):
            c1 = path.rfind("/", 0, len(path))
        else:
            i = path.rfind("/", 0, (startIndex + 1))
            startLeft = (max(0,((startIndex + 1) - len("/"))) if ((i == -1)) else (i + 1))
            check = path.find("/", startLeft, len(path))
            c1 = (check if (((check > i) and ((check <= startIndex)))) else i)
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Path.hx:84
        startIndex = None
        c2 = None
        if (startIndex is None):
            c2 = path.rfind("\\", 0, len(path))
        else:
            i = path.rfind("\\", 0, (startIndex + 1))
            startLeft = (max(0,((startIndex + 1) - len("\\"))) if ((i == -1)) else (i + 1))
            check = path.find("\\", startLeft, len(path))
            c2 = (check if (((check > i) and ((check <= startIndex)))) else i)
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Path.hx:85
        if (c1 < c2):
            # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Path.hx:86
            self.dir = HxString.substr(path,0,c2)
            # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Path.hx:87
            path = HxString.substr(path,(c2 + 1),None)
            # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Path.hx:88
            self.backslash = True
        elif (c2 < c1):
            # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Path.hx:90
            self.dir = HxString.substr(path,0,c1)
            # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Path.hx:91
            path = HxString.substr(path,(c1 + 1),None)
        else:
            self.dir = None
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Path.hx:94
        startIndex = None
        cp = None
        if (startIndex is None):
            cp = path.rfind(".", 0, len(path))
        else:
            i = path.rfind(".", 0, (startIndex + 1))
            startLeft = (max(0,((startIndex + 1) - len("."))) if ((i == -1)) else (i + 1))
            check = path.find(".", startLeft, len(path))
            cp = (check if (((check > i) and ((check <= startIndex)))) else i)
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Path.hx:95
        if (cp != -1):
            # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Path.hx:96
            self.ext = HxString.substr(path,(cp + 1),None)
            # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Path.hx:97
            self.file = HxString.substr(path,0,cp)
        else:
            # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Path.hx:99
            self.ext = None
            # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Path.hx:100
            self.file = path

    def toString(self):
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Path.hx:115
        return ((HxOverrides.stringOrNull((("" if ((self.dir is None)) else (HxOverrides.stringOrNull(self.dir) + HxOverrides.stringOrNull((("\\" if (self.backslash) else "/"))))))) + HxOverrides.stringOrNull(self.file)) + HxOverrides.stringOrNull((("" if ((self.ext is None)) else ("." + HxOverrides.stringOrNull(self.ext))))))

    @staticmethod
    def isAbsolute(path):
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Path.hx:315
        if path.startswith("/"):
            return True
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Path.hx:317
        if ((("" if ((1 >= len(path))) else path[1])) == ":"):
            return True
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Path.hx:319
        if path.startswith("\\\\"):
            return True
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Path.hx:321
        return False

haxe_io_Path._hx_class = haxe_io_Path


class HxString:
    _hx_class_name = "HxString"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["split", "charCodeAt", "charAt", "lastIndexOf", "toUpperCase", "toLowerCase", "indexOf", "indexOfImpl", "toString", "substring", "substr"]

    @staticmethod
    def split(s,d):
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/StringImpl.hx:31
        if (d == ""):
            return list(s)
        else:
            return s.split(d)

    @staticmethod
    def charCodeAt(s,index):
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/StringImpl.hx:36
        if ((((s is None) or ((len(s) == 0))) or ((index < 0))) or ((index >= len(s)))):
            return None
        else:
            return ord(s[index])

    @staticmethod
    def charAt(s,index):
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/StringImpl.hx:41
        if ((index < 0) or ((index >= len(s)))):
            return ""
        else:
            return s[index]

    @staticmethod
    def lastIndexOf(s,_hx_str,startIndex = None):
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/StringImpl.hx:46
        if (startIndex is None):
            return s.rfind(_hx_str, 0, len(s))
        elif (_hx_str == ""):
            # /Users/glen/bin/haxe-4.2.5/std/python/internal/StringImpl.hx:49
            length = len(s)
            # /Users/glen/bin/haxe-4.2.5/std/python/internal/StringImpl.hx:50
            if (startIndex < 0):
                # /Users/glen/bin/haxe-4.2.5/std/python/internal/StringImpl.hx:51
                startIndex = (length + startIndex)
                # /Users/glen/bin/haxe-4.2.5/std/python/internal/StringImpl.hx:52
                if (startIndex < 0):
                    startIndex = 0
            # /Users/glen/bin/haxe-4.2.5/std/python/internal/StringImpl.hx:54
            if (startIndex > length):
                return length
            else:
                return startIndex
        else:
            # /Users/glen/bin/haxe-4.2.5/std/python/internal/StringImpl.hx:56
            i = s.rfind(_hx_str, 0, (startIndex + 1))
            # /Users/glen/bin/haxe-4.2.5/std/python/internal/StringImpl.hx:57
            startLeft = (max(0,((startIndex + 1) - len(_hx_str))) if ((i == -1)) else (i + 1))
            # /Users/glen/bin/haxe-4.2.5/std/python/internal/StringImpl.hx:58
            check = s.find(_hx_str, startLeft, len(s))
            # /Users/glen/bin/haxe-4.2.5/std/python/internal/StringImpl.hx:59
            if ((check > i) and ((check <= startIndex))):
                return check
            else:
                return i

    @staticmethod
    def toUpperCase(s):
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/StringImpl.hx:69
        return s.upper()

    @staticmethod
    def toLowerCase(s):
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/StringImpl.hx:74
        return s.lower()

    @staticmethod
    def indexOf(s,_hx_str,startIndex = None):
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/StringImpl.hx:79
        if (startIndex is None):
            return s.find(_hx_str)
        else:
            return HxString.indexOfImpl(s,_hx_str,startIndex)

    @staticmethod
    def indexOfImpl(s,_hx_str,startIndex):
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/StringImpl.hx:86
        if (_hx_str == ""):
            # /Users/glen/bin/haxe-4.2.5/std/python/internal/StringImpl.hx:87
            length = len(s)
            # /Users/glen/bin/haxe-4.2.5/std/python/internal/StringImpl.hx:88
            if (startIndex < 0):
                # /Users/glen/bin/haxe-4.2.5/std/python/internal/StringImpl.hx:89
                startIndex = (length + startIndex)
                # /Users/glen/bin/haxe-4.2.5/std/python/internal/StringImpl.hx:90
                if (startIndex < 0):
                    startIndex = 0
            # /Users/glen/bin/haxe-4.2.5/std/python/internal/StringImpl.hx:92
            if (startIndex > length):
                return length
            else:
                return startIndex
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/StringImpl.hx:94
        return s.find(_hx_str, startIndex)

    @staticmethod
    def toString(s):
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/StringImpl.hx:99
        return s

    @staticmethod
    def substring(s,startIndex,endIndex = None):
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/StringImpl.hx:118
        if (startIndex < 0):
            startIndex = 0
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/StringImpl.hx:120
        if (endIndex is None):
            return s[startIndex:]
        else:
            # /Users/glen/bin/haxe-4.2.5/std/python/internal/StringImpl.hx:123
            if (endIndex < 0):
                endIndex = 0
            # /Users/glen/bin/haxe-4.2.5/std/python/internal/StringImpl.hx:125
            if (endIndex < startIndex):
                return s[endIndex:startIndex]
            else:
                return s[startIndex:endIndex]

    @staticmethod
    def substr(s,startIndex,_hx_len = None):
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/StringImpl.hx:135
        if (_hx_len is None):
            return s[startIndex:]
        else:
            # /Users/glen/bin/haxe-4.2.5/std/python/internal/StringImpl.hx:138
            if (_hx_len == 0):
                return ""
            # /Users/glen/bin/haxe-4.2.5/std/python/internal/StringImpl.hx:140
            if (startIndex < 0):
                # /Users/glen/bin/haxe-4.2.5/std/python/internal/StringImpl.hx:141
                startIndex = (len(s) + startIndex)
                # /Users/glen/bin/haxe-4.2.5/std/python/internal/StringImpl.hx:142
                if (startIndex < 0):
                    startIndex = 0
            # /Users/glen/bin/haxe-4.2.5/std/python/internal/StringImpl.hx:145
            return s[startIndex:(startIndex + _hx_len)]
HxString._hx_class = HxString


class python_HaxeIterator:
    _hx_class_name = "python.HaxeIterator"
    _hx_is_interface = "False"
    __slots__ = ("it", "x", "has", "checked")
    _hx_fields = ["it", "x", "has", "checked"]
    _hx_methods = ["next", "hasNext"]

    def __init__(self,it):
        # /Users/glen/bin/haxe-4.2.5/std/python/HaxeIterator.hx:32
        self.checked = False
        # /Users/glen/bin/haxe-4.2.5/std/python/HaxeIterator.hx:31
        self.has = False
        # /Users/glen/bin/haxe-4.2.5/std/python/HaxeIterator.hx:30
        self.x = None
        # /Users/glen/bin/haxe-4.2.5/std/python/HaxeIterator.hx:35
        self.it = it

    def next(self):
        # /Users/glen/bin/haxe-4.2.5/std/python/HaxeIterator.hx:39
        if (not self.checked):
            self.hasNext()
        # /Users/glen/bin/haxe-4.2.5/std/python/HaxeIterator.hx:41
        self.checked = False
        # /Users/glen/bin/haxe-4.2.5/std/python/HaxeIterator.hx:42
        return self.x

    def hasNext(self):
        # /Users/glen/bin/haxe-4.2.5/std/python/HaxeIterator.hx:46
        if (not self.checked):
            # /Users/glen/bin/haxe-4.2.5/std/python/HaxeIterator.hx:47
            try:
                # /Users/glen/bin/haxe-4.2.5/std/python/HaxeIterator.hx:48
                self.x = self.it.__next__()
                # /Users/glen/bin/haxe-4.2.5/std/python/HaxeIterator.hx:49
                self.has = True
            except BaseException as _g:
                # /Users/glen/bin/haxe-4.2.5/std/python/HaxeIterator.hx:50
                None
                # /Users/glen/bin/haxe-4.2.5/std/python/HaxeIterator.hx:47
                if Std.isOfType(haxe_Exception.caught(_g).unwrap(),StopIteration):
                    # /Users/glen/bin/haxe-4.2.5/std/python/HaxeIterator.hx:51
                    self.has = False
                    # /Users/glen/bin/haxe-4.2.5/std/python/HaxeIterator.hx:52
                    self.x = None
                else:
                    raise _g
            # /Users/glen/bin/haxe-4.2.5/std/python/HaxeIterator.hx:54
            self.checked = True
        # /Users/glen/bin/haxe-4.2.5/std/python/HaxeIterator.hx:56
        return self.has

python_HaxeIterator._hx_class = python_HaxeIterator


class a8_UserConfig:
    _hx_class_name = "a8.UserConfig"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["repoConfig", "getRepoProp", "hasRepoProp", "repo_url", "versionsVersion", "versionsVersionFromRepo"]

    @staticmethod
    def getRepoProp(repoPrefix,suffix):
        # src/a8/UserConfig.hx:26
        name = ((("null" if repoPrefix is None else repoPrefix) + "_") + ("null" if suffix is None else suffix))
        # src/a8/UserConfig.hx:27
        v = a8_UserConfig.repoConfig.h.get(name,None)
        # src/a8/UserConfig.hx:28
        if (v is None):
            raise haxe_Exception.thrown((("no " + ("null" if name is None else name)) + " defined in ~/.a8/repo.properties"))
        # src/a8/UserConfig.hx:31
        return v

    @staticmethod
    def hasRepoProp(repoPrefix,suffix):
        # src/a8/UserConfig.hx:35
        name = ((("null" if repoPrefix is None else repoPrefix) + "_") + ("null" if suffix is None else suffix))
        # src/a8/UserConfig.hx:36
        v = a8_UserConfig.repoConfig.h.get(name,None)
        # src/a8/UserConfig.hx:37
        return (v is not None)

    @staticmethod
    def repo_url(repoPrefix):
        # src/a8/UserConfig.hx:41
        if a8_UserConfig.hasRepoProp(repoPrefix,"url"):
            # src/a8/UserConfig.hx:43
            url = a8_UserConfig.getRepoProp(repoPrefix,"url")
            # src/a8/UserConfig.hx:45
            if (a8_UserConfig.hasRepoProp(repoPrefix,"user") and a8_UserConfig.hasRepoProp(repoPrefix,"password")):
                # src/a8/UserConfig.hx:46
                u = a8_UserConfig.getRepoProp(repoPrefix,"user")
                # src/a8/UserConfig.hx:47
                p = a8_UserConfig.getRepoProp(repoPrefix,"password")
                # src/a8/UserConfig.hx:49
                separator = "://"
                # src/a8/UserConfig.hx:50
                split = (list(url) if ((separator == "")) else url.split(separator))
                # src/a8/UserConfig.hx:51
                url = ((((((HxOverrides.stringOrNull((split[0] if 0 < len(split) else None)) + ("null" if separator is None else separator)) + ("null" if u is None else u)) + ":") + ("null" if p is None else p)) + "@") + HxOverrides.stringOrNull((split[1] if 1 < len(split) else None)))
            # src/a8/UserConfig.hx:54
            return url
        elif (repoPrefix == "maven"):
            return "https://repo.maven.apache.org/maven2/"
        else:
            raise haxe_Exception.thrown(("unable to find repo " + ("null" if repoPrefix is None else repoPrefix)))

    @staticmethod
    def versionsVersion(repoPrefix):
        # src/a8/UserConfig.hx:64
        version = a8_UserConfig.repoConfig.h.get("versions_version",None)
        # src/a8/UserConfig.hx:65
        if (version is None):
            version = a8_UserConfig.versionsVersionFromRepo(repoPrefix)
        # src/a8/UserConfig.hx:68
        return version

    @staticmethod
    def versionsVersionFromRepo(repoPrefix):
        # src/a8/UserConfig.hx:72
        v = a8_UserConfig.getRepoProp(repoPrefix,"url")
        # src/a8/UserConfig.hx:73
        startIndex = None
        startIndex1 = (((v.find("://") if ((startIndex is None)) else HxString.indexOfImpl(v,"://",startIndex))) + 1)
        url = (HxOverrides.stringOrNull(HxString.substring(v,0,(v.find("/") if ((startIndex1 is None)) else HxString.indexOfImpl(v,"/",startIndex1)))) + "/versionsVersion")
        # src/a8/UserConfig.hx:74
        return sys_Http.requestUrl(url)
a8_UserConfig._hx_class = a8_UserConfig


class a8_launcher_CommandLineProcessor:
    _hx_class_name = "a8.launcher.CommandLineProcessor"
    _hx_is_interface = "False"
    __slots__ = ("lazy_argDefs",)
    _hx_fields = ["lazy_argDefs"]
    _hx_methods = ["apply", "get_argDefs"]

    def __init__(self):
        # src/a8/launcher/CommandLineProcessor.hx:9
        self.lazy_argDefs = None
        def _hx_local_5():
            def _hx_local_4():
                # src/a8/launcher/CommandLineProcessor.hx:14
                def _hx_local_0(config,args):
                    # src/a8/launcher/CommandLineProcessor.hx:14
                    Reflect.setField(config,"explicitVersion",args)
                # src/a8/launcher/CommandLineProcessor.hx:21
                def _hx_local_1(config,args):
                    # src/a8/launcher/CommandLineProcessor.hx:21
                    Reflect.setField(config,"quiet",a8_OptionOps.isEmpty(args))
                # src/a8/launcher/CommandLineProcessor.hx:28
                def _hx_local_2(config,args):
                    # src/a8/launcher/CommandLineProcessor.hx:28
                    Reflect.setField(config,"resolveOnly",a8_OptionOps.nonEmpty(args))
                # src/a8/launcher/CommandLineProcessor.hx:35
                def _hx_local_3(config,args):
                    # src/a8/launcher/CommandLineProcessor.hx:35
                    Reflect.setField(config,"showHelp",a8_OptionOps.nonEmpty(args))
                # src/a8/launcher/CommandLineProcessor.hx:9
                return [_hx_AnonObject({'name': "--l-version", 'parmCount': 1, 'apply': _hx_local_0, 'processed': False}), _hx_AnonObject({'name': "--l-verbose", 'parmCount': 0, 'apply': _hx_local_1, 'processed': False}), _hx_AnonObject({'name': "--l-resolveOnly", 'parmCount': 0, 'apply': _hx_local_2, 'processed': False}), _hx_AnonObject({'name': "--l-help", 'parmCount': 0, 'apply': _hx_local_3, 'processed': False})]
            return _hx_local_4()
        self.lazy_argDefs = tink_core__Lazy_LazyFunc(_hx_local_5)

    def apply(self,initialConfig):
        # src/a8/launcher/CommandLineProcessor.hx:44
        config = Reflect.copy(initialConfig)
        # src/a8/launcher/CommandLineProcessor.hx:46
        newArgs = []
        # src/a8/launcher/CommandLineProcessor.hx:47
        Reflect.setField(config,"resolvedCommandLineArgs",newArgs)
        # src/a8/launcher/CommandLineProcessor.hx:48
        temp = list(Reflect.field(initialConfig,"rawCommandLineArgs"))
        # src/a8/launcher/CommandLineProcessor.hx:51
        temp.reverse()
        # src/a8/launcher/CommandLineProcessor.hx:52
        if (len(temp) != 0):
            temp.pop()
        # src/a8/launcher/CommandLineProcessor.hx:54
        while (len(temp) > 0):
            # src/a8/launcher/CommandLineProcessor.hx:55
            a = [(None if ((len(temp) == 0)) else temp.pop())]
            # src/a8/launcher/CommandLineProcessor.hx:56
            def _hx_local_1(a):
                # src/a8/launcher/CommandLineProcessor.hx:56
                def _hx_local_0(ad):
                    # src/a8/launcher/CommandLineProcessor.hx:56
                    return (ad.name == (a[0] if 0 < len(a) else None))
                return _hx_local_0
            argDef = Lambda.find(self.get_argDefs(),_hx_local_1(a))
            # src/a8/launcher/CommandLineProcessor.hx:57
            if (argDef is None):
                # src/a8/launcher/CommandLineProcessor.hx:58
                if (a[0] if 0 < len(a) else None).startswith("--l-"):
                    raise haxe_Exception.thrown(a8_Exception(("don't know how to handle arg -- " + HxOverrides.stringOrNull((a[0] if 0 < len(a) else None))),None,_hx_AnonObject({'fileName': "src/a8/launcher/CommandLineProcessor.hx", 'lineNumber': 59, 'className': "a8.launcher.CommandLineProcessor", 'methodName': "apply"})))
                # src/a8/launcher/CommandLineProcessor.hx:61
                newArgs.append((a[0] if 0 < len(a) else None))
            else:
                # src/a8/launcher/CommandLineProcessor.hx:63
                parms = None
                # src/a8/launcher/CommandLineProcessor.hx:64
                if (argDef.parmCount == 0):
                    parms = haxe_ds_Option.Some(argDef.name)
                elif (argDef.parmCount == 1):
                    parms = haxe_ds_Option.Some((None if ((len(temp) == 0)) else temp.pop()))
                else:
                    raise haxe_Exception.thrown(a8_Exception("can only handle parmCount of 0 or 1",None,_hx_AnonObject({'fileName': "src/a8/launcher/CommandLineProcessor.hx", 'lineNumber': 66, 'className': "a8.launcher.CommandLineProcessor", 'methodName': "apply"})))
                # src/a8/launcher/CommandLineProcessor.hx:67
                argDef.apply(config,parms)
                # src/a8/launcher/CommandLineProcessor.hx:68
                Reflect.setField(argDef,"processed",True)
        # src/a8/launcher/CommandLineProcessor.hx:74
        def _hx_local_2(ad):
            # src/a8/launcher/CommandLineProcessor.hx:74
            if (not Reflect.field(ad,"processed")):
                ad.apply(config,haxe_ds_Option._hx_None)
        # src/a8/launcher/CommandLineProcessor.hx:73
        Lambda.iter(self.get_argDefs(),_hx_local_2)
        # src/a8/launcher/CommandLineProcessor.hx:81
        return config

    def get_argDefs(self):
        # src/a8/launcher/CommandLineProcessor.hx:9
        return tink_core__Lazy_Lazy_Impl_.get(self.lazy_argDefs)

a8_launcher_CommandLineProcessor._hx_class = a8_launcher_CommandLineProcessor


class a8_launcher_Launcher:
    _hx_class_name = "a8.launcher.Launcher"
    _hx_is_interface = "False"
    __slots__ = ("lazy_logArchivesDir", "lazy_logsDir", "lazy_installDir", "lazy_a8VersionsCache", "config", "appName", "initialArgs", "pipedStdout", "pipedStderr", "logRollers")
    _hx_fields = ["lazy_logArchivesDir", "lazy_logsDir", "lazy_installDir", "lazy_a8VersionsCache", "config", "appName", "initialArgs", "pipedStdout", "pipedStderr", "logRollers"]
    _hx_methods = ["logTrace", "logWarn", "_log", "archiveOldLogs", "archiveLogFiles", "resolveStandardArgs", "resolveJvmCliLaunchArgs", "resolveJvmLaunchArgs", "runAndWait", "initializeLogRollers", "get_a8VersionsCache", "get_installDir", "get_logsDir", "get_logArchivesDir"]
    _hx_statics = ["initDirectory"]

    def __init__(self,config,appName,initialArgs):
        # src/a8/launcher/Launcher.hx:36
        self.logRollers = None
        # src/a8/launcher/Launcher.hx:35
        self.pipedStderr = None
        # src/a8/launcher/Launcher.hx:34
        self.pipedStdout = None
        # src/a8/launcher/Launcher.hx:24
        self.initialArgs = None
        # src/a8/launcher/Launcher.hx:22
        self.appName = None
        # src/a8/launcher/Launcher.hx:21
        self.config = None
        # src/a8/launcher/Launcher.hx:27
        self.lazy_a8VersionsCache = None
        # src/a8/launcher/Launcher.hx:30
        self.lazy_installDir = None
        # src/a8/launcher/Launcher.hx:31
        self.lazy_logsDir = None
        # src/a8/launcher/Launcher.hx:32
        self.lazy_logArchivesDir = None
        # /usr/local/lib/haxe/lib/tink_syntaxhub/0,5,0/src/tink/SyntaxHub.hx:35
        _gthis = self
        # src/a8/launcher/Launcher.hx:32
        def _hx_local_0():
            # src/a8/launcher/Launcher.hx:32
            return a8_launcher_Launcher.initDirectory("archives",None,_gthis.get_logsDir(),Reflect.field(_gthis.config,"logFiles"))
        self.lazy_logArchivesDir = tink_core__Lazy_LazyFunc(_hx_local_0)
        # src/a8/launcher/Launcher.hx:31
        def _hx_local_1():
            # src/a8/launcher/Launcher.hx:31
            return a8_launcher_Launcher.initDirectory(Reflect.field(config,"logsDir"),"logs",_gthis.get_installDir())
        self.lazy_logsDir = tink_core__Lazy_LazyFunc(_hx_local_1)
        # src/a8/launcher/Launcher.hx:30
        def _hx_local_2():
            # src/a8/launcher/Launcher.hx:30
            return a8_launcher_Launcher.initDirectory(Reflect.field(config,"installDir"),None,a8_PathOps.path(python_lib_Os.getcwd()))
        self.lazy_installDir = tink_core__Lazy_LazyFunc(_hx_local_2)
        # src/a8/launcher/Launcher.hx:27
        def _hx_local_3():
            # src/a8/launcher/Launcher.hx:27
            return a8_launcher_Launcher.initDirectory(".a8/versions/cache",None,a8_PathOps.userHome())
        self.lazy_a8VersionsCache = tink_core__Lazy_LazyFunc(_hx_local_3)
        # src/a8/launcher/Launcher.hx:21
        self.config = config
        # src/a8/launcher/Launcher.hx:22
        self.appName = appName
        # src/a8/launcher/Launcher.hx:24
        self.initialArgs = initialArgs

    def logTrace(self,msg,posInfo = None):
        # src/a8/launcher/Launcher.hx:60
        if (not Reflect.field(self.config,"quiet")):
            if (self.pipedStdout is not None):
                self.pipedStdout.log(("TRACE - " + ("null" if msg is None else msg)))
            else:
                a8_Logger.trace(msg,posInfo)

    def logWarn(self,msg,posInfo = None):
        # src/a8/launcher/Launcher.hx:70
        if (self.pipedStderr is not None):
            self.pipedStderr.log(("WARN - " + ("null" if msg is None else msg)))
        else:
            a8_Logger.warn(msg,posInfo)

    def _log(self,msg,pipe):
        pass

    def archiveOldLogs(self):
        # src/a8/launcher/Launcher.hx:82
        prefix = (HxOverrides.stringOrNull(self.appName) + ".")
        # src/a8/launcher/Launcher.hx:83
        suffix1 = ".details"
        # src/a8/launcher/Launcher.hx:84
        suffix2 = ".errors"
        # src/a8/launcher/Launcher.hx:89
        def _hx_local_0(f):
            # src/a8/launcher/Launcher.hx:90
            filename = a8_PathOps.basename(f)
            # src/a8/launcher/Launcher.hx:91
            if filename.startswith(prefix):
                if (not filename.endswith(suffix1)):
                    return filename.endswith(suffix2)
                else:
                    return True
            else:
                return False
        # src/a8/launcher/Launcher.hx:86
        filesToArchive = list(filter(_hx_local_0,a8_PathOps.files(self.get_logsDir())))
        # src/a8/launcher/Launcher.hx:96
        self.archiveLogFiles(filesToArchive)

    def archiveLogFiles(self,files):
        # src/a8/launcher/Launcher.hx:100
        _gthis = self
        # src/a8/launcher/Launcher.hx:104
        def _hx_local_0(f):
            # src/a8/launcher/Launcher.hx:105
            target = a8_PathOps.entry(_gthis.get_logArchivesDir(),a8_PathOps.basename(f))
            # src/a8/launcher/Launcher.hx:106
            a8_PathOps.deleteFile(target)
            # src/a8/launcher/Launcher.hx:107
            a8_PathOps.moveTo(f,target)
            # src/a8/launcher/Launcher.hx:108
            return target
        # src/a8/launcher/Launcher.hx:102
        archivedFiles = list(map(_hx_local_0,files))
        # src/a8/launcher/Launcher.hx:111
        self.logTrace(("archiving log files -- " + Std.string(archivedFiles)),_hx_AnonObject({'fileName': "src/a8/launcher/Launcher.hx", 'lineNumber': 111, 'className': "a8.launcher.Launcher", 'methodName': "archiveLogFiles"}))
        # src/a8/launcher/Launcher.hx:114
        def _hx_local_2():
            # src/a8/launcher/Launcher.hx:115
            def _hx_local_1(f):
                # src/a8/launcher/Launcher.hx:115
                python_lib_Subprocess.call(["gzip", "-f", a8_PathOps.realPathStr(f)])
            # src/a8/launcher/Launcher.hx:114
            Lambda.iter(archivedFiles,_hx_local_1)
        # src/a8/launcher/Launcher.hx:113
        gzipFiles = _hx_local_2
        # src/a8/launcher/Launcher.hx:119
        a8_PyOps.spawn(gzipFiles)

    def resolveStandardArgs(self,stdlauncher):
        # src/a8/launcher/Launcher.hx:124
        launchConfig = stdlauncher
        # src/a8/launcher/Launcher.hx:125
        return _hx_AnonObject({'kind': "popen", 'args': stdlauncher.args, 'env': None, 'cwd': None, 'executable': None})

    def resolveJvmCliLaunchArgs(self,jvmlauncher):
        # src/a8/launcher/Launcher.hx:135
        versionFile = None
        # src/a8/launcher/Launcher.hx:136
        if a8_OptionOps.nonEmpty(Reflect.field(self.config,"explicitVersion")):
            versionFile = (HxOverrides.stringOrNull(a8_OptionOps.getOrError(Reflect.field(self.config,"explicitVersion"),"")) + ".json")
        elif (Reflect.field(jvmlauncher,"branch") is not None):
            versionFile = (("latest_" + HxOverrides.stringOrNull(Reflect.field(jvmlauncher,"branch"))) + ".json")
        elif (Reflect.field(jvmlauncher,"version") is not None):
            versionFile = (HxOverrides.stringOrNull(Reflect.field(jvmlauncher,"version")) + ".json")
        else:
            raise haxe_Exception.thrown(a8_Exception("must provide a config with branch or version",None,_hx_AnonObject({'fileName': "src/a8/launcher/Launcher.hx", 'lineNumber': 143, 'className': "a8.launcher.Launcher", 'methodName': "resolveJvmCliLaunchArgs"})))
        # src/a8/launcher/Launcher.hx:145
        inventoryFile = a8_PathOps.entry(self.get_a8VersionsCache(),((((HxOverrides.stringOrNull(jvmlauncher.organization) + "/") + HxOverrides.stringOrNull(jvmlauncher.artifact)) + "/") + ("null" if versionFile is None else versionFile)))
        # src/a8/launcher/Launcher.hx:146
        a8_Logger.trace(("using inventory file - " + HxOverrides.stringOrNull(inventoryFile.toString())),_hx_AnonObject({'fileName': "src/a8/launcher/Launcher.hx", 'lineNumber': 146, 'className': "a8.launcher.Launcher", 'methodName': "resolveJvmCliLaunchArgs"}))
        # src/a8/launcher/Launcher.hx:147
        if ((not a8_PathOps.exists(inventoryFile)) or Reflect.field(self.config,"resolveOnly")):
            # src/a8/launcher/Launcher.hx:148
            _hx_exec = a8_Exec()
            # src/a8/launcher/Launcher.hx:154
            version = a8_OptionOps.getOrElse(a8_OptionOps.toOption(a8_UserConfig.repoConfig.h.get("versions_version",None)),a8_Constants.a8VersionsVersion)
            # src/a8/launcher/Launcher.hx:156
            repoPrefix = "repo"
            # src/a8/launcher/Launcher.hx:157
            if (Reflect.field(jvmlauncher,"repo") is not None):
                repoPrefix = Reflect.field(jvmlauncher,"repo")
            # src/a8/launcher/Launcher.hx:160
            repoUrl = a8_UserConfig.repo_url(repoPrefix)
            # src/a8/launcher/Launcher.hx:162
            def _hx_local_0():
                # src/a8/launcher/Launcher.hx:162
                _hx_exec.args = [(Std.string(a8_PathOps.parent(a8_PathOps.programPath())) + "/coursier"), "launch", "--repository", repoUrl, ("io.accur8:a8-versions_2.13:" + ("null" if version is None else version)), "-M", "a8.versions.apps.Main", "--", "resolve", "--organization", jvmlauncher.organization, "--artifact", jvmlauncher.artifact, "--repo", repoPrefix]
                return _hx_exec.args
            args = _hx_local_0()
            # src/a8/launcher/Launcher.hx:163
            # src/a8/launcher/Launcher.hx:163
            _hx_str = Std.string(("running -- " + HxOverrides.stringOrNull(" ".join([python_Boot.toString1(x1,'') for x1 in args]))))
            python_Lib.printString((("" + ("null" if _hx_str is None else _hx_str)) + HxOverrides.stringOrNull(python_Lib.lineEnd)))
            # src/a8/launcher/Launcher.hx:164
            if a8_OptionOps.nonEmpty(Reflect.field(self.config,"explicitVersion")):
                # src/a8/launcher/Launcher.hx:165
                args.append("--version")
                # src/a8/launcher/Launcher.hx:166
                # src/a8/launcher/Launcher.hx:166
                x = a8_OptionOps.get(Reflect.field(self.config,"explicitVersion"))
                args.append(x)
            elif (Reflect.field(jvmlauncher,"branch") is not None):
                # src/a8/launcher/Launcher.hx:168
                args.append("--branch")
                # src/a8/launcher/Launcher.hx:169
                # src/a8/launcher/Launcher.hx:169
                x = Reflect.field(jvmlauncher,"branch")
                args.append(x)
            elif (Reflect.field(jvmlauncher,"version") is not None):
                # src/a8/launcher/Launcher.hx:171
                args.append("--version")
                # src/a8/launcher/Launcher.hx:172
                # src/a8/launcher/Launcher.hx:172
                x = Reflect.field(jvmlauncher,"version")
                args.append(x)
            # src/a8/launcher/Launcher.hx:174
            _hx_exec.execInline()
            # src/a8/launcher/Launcher.hx:175
            # src/a8/launcher/Launcher.hx:175
            _hx_str = Std.string(("completed running -- " + HxOverrides.stringOrNull(" ".join([python_Boot.toString1(x1,'') for x1 in args]))))
            python_Lib.printString((("" + ("null" if _hx_str is None else _hx_str)) + HxOverrides.stringOrNull(python_Lib.lineEnd)))
        # src/a8/launcher/Launcher.hx:177
        la = self.resolveJvmLaunchArgs(jvmlauncher,inventoryFile,False)
        # src/a8/launcher/Launcher.hx:179
        la.kind = "exec"
        # src/a8/launcher/Launcher.hx:180
        la.cwd = None
        # src/a8/launcher/Launcher.hx:182
        return la

    def resolveJvmLaunchArgs(self,jvmlauncher,installInventoryFile,createAppNameSymlink):
        # src/a8/launcher/Launcher.hx:188
        if (not a8_PathOps.exists(installInventoryFile)):
            raise haxe_Exception.thrown(a8_Exception(("inventory file does not exist " + HxOverrides.stringOrNull(installInventoryFile.toString())),None,_hx_AnonObject({'fileName': "src/a8/launcher/Launcher.hx", 'lineNumber': 189, 'className': "a8.launcher.Launcher", 'methodName': "resolveJvmLaunchArgs"})))
        # src/a8/launcher/Launcher.hx:192
        launchConfig = jvmlauncher
        # src/a8/launcher/Launcher.hx:194
        config = python_lib_Json.loads(a8_PathOps.readText(installInventoryFile),**python__KwArgs_KwArgs_Impl_.fromT(_hx_AnonObject({'object_hook': python_Lib.dictToAnon})))
        # src/a8/launcher/Launcher.hx:196
        launcherD = jvmlauncher
        # src/a8/launcher/Launcher.hx:198
        def _hx_local_0(e):
            # src/a8/launcher/Launcher.hx:199
            p = a8_PathOps.realPathStr(e)
            # src/a8/launcher/Launcher.hx:200
            if (p.endswith(".jar") or a8_PathOps.isDir(e)):
                # src/a8/launcher/Launcher.hx:201
                _this = config.classpath
                _this.append(p)
        Lambda.iter(a8_PathOps.entries(a8_PathOps.entry(self.get_installDir(),"lib")),_hx_local_0)
        # src/a8/launcher/Launcher.hx:204
        _this = config.classpath
        classpath = ":".join([python_Boot.toString1(x1,'') for x1 in _this])
        # src/a8/launcher/Launcher.hx:206
        args = list()
        # src/a8/launcher/Launcher.hx:208
        if createAppNameSymlink:
            # src/a8/launcher/Launcher.hx:209
            symlinkName = ("j_" + HxOverrides.stringOrNull(self.appName))
            # src/a8/launcher/Launcher.hx:210
            symlinkParent = self.get_installDir()
            # src/a8/launcher/Launcher.hx:211
            javaAppNameSymLink = ((HxOverrides.stringOrNull(a8_PathOps.realPathStr(symlinkParent)) + "/") + ("null" if symlinkName is None else symlinkName))
            # src/a8/launcher/Launcher.hx:212
            javaAppNameSymLinkPath = a8_PathOps.path(javaAppNameSymLink)
            # src/a8/launcher/Launcher.hx:213
            cmd = None
            # src/a8/launcher/Launcher.hx:214
            if (not a8_PathOps.isFile(javaAppNameSymLinkPath)):
                # src/a8/launcher/Launcher.hx:215
                javaExec = a8_PyShutil2.which("java")
                # src/a8/launcher/Launcher.hx:216
                a8_Logger.trace(((("creating symlink " + ("null" if javaExec is None else javaExec)) + " --> ") + ("null" if javaAppNameSymLink is None else javaAppNameSymLink)),_hx_AnonObject({'fileName': "src/a8/launcher/Launcher.hx", 'lineNumber': 216, 'className': "a8.launcher.Launcher", 'methodName': "resolveJvmLaunchArgs"}))
                # src/a8/launcher/Launcher.hx:217
                a8_PyOs2.symlink(javaExec,javaAppNameSymLink)
                # src/a8/launcher/Launcher.hx:213
                cmd = (("./" + ("null" if symlinkName is None else symlinkName)) if (a8_PathOps.isFile(javaAppNameSymLinkPath)) else "java")
            else:
                cmd = ("./" + ("null" if symlinkName is None else symlinkName))
            # src/a8/launcher/Launcher.hx:226
            args.append(cmd)
        else:
            args.append("java")
        # src/a8/launcher/Launcher.hx:231
        # src/a8/launcher/Launcher.hx:231
        x = ("-DappName=" + HxOverrides.stringOrNull(self.appName))
        args.append(x)
        # src/a8/launcher/Launcher.hx:233
        if (Reflect.field(launcherD,"jvmArgs") is not None):
            # src/a8/launcher/Launcher.hx:235
            def _hx_local_1(jvmArg):
                # src/a8/launcher/Launcher.hx:235
                args.append(jvmArg)
            # src/a8/launcher/Launcher.hx:234
            Lambda.iter(Reflect.field(jvmlauncher,"jvmArgs"),_hx_local_1)
        # src/a8/launcher/Launcher.hx:240
        # src/a8/launcher/Launcher.hx:240
        x = jvmlauncher.mainClass
        args.append(x)
        # src/a8/launcher/Launcher.hx:242
        if (Reflect.field(launcherD,"args") is not None):
            # src/a8/launcher/Launcher.hx:244
            def _hx_local_2(arg):
                # src/a8/launcher/Launcher.hx:244
                args.append(arg)
            # src/a8/launcher/Launcher.hx:243
            Lambda.iter(Reflect.field(jvmlauncher,"args"),_hx_local_2)
        # src/a8/launcher/Launcher.hx:248
        def _hx_local_3(arg):
            # src/a8/launcher/Launcher.hx:248
            args.append(arg)
        # src/a8/launcher/Launcher.hx:247
        Lambda.iter(Reflect.field(self.config,"resolvedCommandLineArgs"),_hx_local_3)
        # src/a8/launcher/Launcher.hx:251
        env = python_lib_Os.environ
        # src/a8/launcher/Launcher.hx:253
        newEnv = env.copy()
        # src/a8/launcher/Launcher.hx:257
        newEnv["CLASSPATH"] = classpath
        # src/a8/launcher/Launcher.hx:258
        newEnv["LAUNCHER_INSTALL_DIR"] = a8_PathOps.realPathStr(self.get_installDir())
        # src/a8/launcher/Launcher.hx:259
        newEnv["LAUNCHER_WORKING_DIR"] = python_lib_Os.getcwd()
        # src/a8/launcher/Launcher.hx:260
        newEnv["LAUNCHER_EXEC_PATH"] = a8_PathOps.realPathStr(a8_PathOps.executablePath())
        # src/a8/launcher/Launcher.hx:262
        return _hx_AnonObject({'kind': "popen", 'args': args, 'env': newEnv, 'cwd': a8_PathOps.realPathStr(self.get_installDir()), 'executable': (args[0] if 0 < len(args) else None)})

    def runAndWait(self):
        # src/a8/launcher/Launcher.hx:275
        self.logTrace(("installDir = " + Std.string(self.get_installDir())),_hx_AnonObject({'fileName': "src/a8/launcher/Launcher.hx", 'lineNumber': 275, 'className': "a8.launcher.Launcher", 'methodName': "runAndWait"}))
        # src/a8/launcher/Launcher.hx:276
        self.logTrace(("logsDir = " + Std.string(self.get_logsDir())),_hx_AnonObject({'fileName': "src/a8/launcher/Launcher.hx", 'lineNumber': 276, 'className': "a8.launcher.Launcher", 'methodName': "runAndWait"}))
        # src/a8/launcher/Launcher.hx:277
        self.logTrace(("logArchivesDir = " + Std.string(self.get_logArchivesDir())),_hx_AnonObject({'fileName': "src/a8/launcher/Launcher.hx", 'lineNumber': 277, 'className': "a8.launcher.Launcher", 'methodName': "runAndWait"}))
        # src/a8/launcher/Launcher.hx:279
        resolvedLaunch = None
        # src/a8/launcher/Launcher.hx:280
        if (self.config.kind == "jvm"):
            # src/a8/launcher/Launcher.hx:281
            installInventoryFile = a8_PathOps.entry(self.get_installDir(),"install-inventory.json")
            # src/a8/launcher/Launcher.hx:279
            resolvedLaunch = self.resolveJvmLaunchArgs(self.config,installInventoryFile,True)
        elif (self.config.kind == "jvm_cli"):
            resolvedLaunch = self.resolveJvmCliLaunchArgs(self.config)
        elif (self.config.kind == "args"):
            resolvedLaunch = self.resolveStandardArgs(self.config)
        else:
            raise haxe_Exception.thrown(a8_Exception(("unable to resolve config kind " + HxOverrides.stringOrNull(self.config.kind)),None,_hx_AnonObject({'fileName': "src/a8/launcher/Launcher.hx", 'lineNumber': 288, 'className': "a8.launcher.Launcher", 'methodName': "runAndWait"})))
        # src/a8/launcher/Launcher.hx:290
        if Reflect.field(self.config,"resolveOnly"):
            return 0
        else:
            # src/a8/launcher/Launcher.hx:294
            if Reflect.field(self.config,"logFiles"):
                self.archiveOldLogs()
            # src/a8/launcher/Launcher.hx:298
            _g = resolvedLaunch.kind
            _hx_local_0 = len(_g)
            # src/a8/launcher/Launcher.hx:299
            if (_hx_local_0 == 4):
                if (_g == "exec"):
                    # src/a8/launcher/Launcher.hx:302
                    if (resolvedLaunch.cwd is not None):
                        python_lib_Os.chdir(resolvedLaunch.cwd)
                    # src/a8/launcher/Launcher.hx:304
                    a8_PyOs2.execvpe(resolvedLaunch.executable,resolvedLaunch.args,resolvedLaunch.env)
                    # src/a8/launcher/Launcher.hx:306
                    raise haxe_Exception.thrown(a8_Exception("this never happens",None,_hx_AnonObject({'fileName': "src/a8/launcher/Launcher.hx", 'lineNumber': 306, 'className': "a8.launcher.Launcher", 'methodName': "runAndWait"})))
                else:
                    raise haxe_Exception.thrown(a8_Exception("don't know how to handle ResolvedLaunch.kind = ${resolvedLaunch.kind}",None,_hx_AnonObject({'fileName': "src/a8/launcher/Launcher.hx", 'lineNumber': 342, 'className': "a8.launcher.Launcher", 'methodName': "runAndWait"})))
            elif (_hx_local_0 == 5):
                if (_g == "popen"):
                    # src/a8/launcher/Launcher.hx:309
                    self.logTrace(("running -- " + Std.string(resolvedLaunch.args)),_hx_AnonObject({'fileName': "src/a8/launcher/Launcher.hx", 'lineNumber': 309, 'className': "a8.launcher.Launcher", 'methodName': "runAndWait"}))
                    # src/a8/launcher/Launcher.hx:311
                    popen = python_lib_subprocess_Popen(resolvedLaunch.args,None,resolvedLaunch.executable,None,python_lib_Subprocess.PIPE,python_lib_Subprocess.PIPE,None,False,False,resolvedLaunch.cwd,resolvedLaunch.env)
                    # src/a8/launcher/Launcher.hx:314
                    def _hx_local_1(out):
                        # src/a8/launcher/Launcher.hx:314
                        out.write((("first output at " + HxOverrides.stringOrNull(a8_PathOps.timestampStr())) + "\n"))
                    # src/a8/launcher/Launcher.hx:313
                    firstIO = _hx_local_1
                    # src/a8/launcher/Launcher.hx:317
                    timestampStr = a8_PathOps.timestampStr()
                    # src/a8/launcher/Launcher.hx:319
                    self.logTrace("setting up pipes",_hx_AnonObject({'fileName': "src/a8/launcher/Launcher.hx", 'lineNumber': 319, 'className': "a8.launcher.Launcher", 'methodName': "runAndWait"}))
                    # src/a8/launcher/Launcher.hx:320
                    self.pipedStdout = a8_launcher_PipedStream(self,a8_StreamOps.asInputStream(popen.stdout),python_lib_Sys.stdout,"details",firstIO,Reflect.field(self.config,"logFiles"),timestampStr)
                    # src/a8/launcher/Launcher.hx:321
                    self.pipedStderr = a8_launcher_PipedStream(self,a8_StreamOps.asInputStream(popen.stderr),python_lib_Sys.stderr,"errors",firstIO,Reflect.field(self.config,"logFiles"),timestampStr)
                    # src/a8/launcher/Launcher.hx:323
                    self.pipedStdout.start()
                    # src/a8/launcher/Launcher.hx:324
                    self.pipedStderr.start()
                    # src/a8/launcher/Launcher.hx:328
                    self.logTrace("initializeLogRollers",_hx_AnonObject({'fileName': "src/a8/launcher/Launcher.hx", 'lineNumber': 328, 'className': "a8.launcher.Launcher", 'methodName': "runAndWait"}))
                    # src/a8/launcher/Launcher.hx:329
                    self.initializeLogRollers()
                    # src/a8/launcher/Launcher.hx:330
                    self.logTrace("initializeLogRollers complete",_hx_AnonObject({'fileName': "src/a8/launcher/Launcher.hx", 'lineNumber': 330, 'className': "a8.launcher.Launcher", 'methodName': "runAndWait"}))
                    # src/a8/launcher/Launcher.hx:333
                    popen.wait()
                    # src/a8/launcher/Launcher.hx:336
                    self.pipedStdout.close()
                    # src/a8/launcher/Launcher.hx:337
                    self.pipedStdout.close()
                    # src/a8/launcher/Launcher.hx:339
                    return popen.returncode
                else:
                    raise haxe_Exception.thrown(a8_Exception("don't know how to handle ResolvedLaunch.kind = ${resolvedLaunch.kind}",None,_hx_AnonObject({'fileName': "src/a8/launcher/Launcher.hx", 'lineNumber': 342, 'className': "a8.launcher.Launcher", 'methodName': "runAndWait"})))
            else:
                raise haxe_Exception.thrown(a8_Exception("don't know how to handle ResolvedLaunch.kind = ${resolvedLaunch.kind}",None,_hx_AnonObject({'fileName': "src/a8/launcher/Launcher.hx", 'lineNumber': 342, 'className': "a8.launcher.Launcher", 'methodName': "runAndWait"})))

    def initializeLogRollers(self):
        # src/a8/launcher/Launcher.hx:348
        _gthis = self
        # src/a8/launcher/Launcher.hx:352
        def _hx_local_0(lr):
            # src/a8/launcher/Launcher.hx:352
            return a8_launcher_LogRollerOps.fromConfig(lr,_gthis)
        # src/a8/launcher/Launcher.hx:349
        self.logRollers = list(map(_hx_local_0,Reflect.field(self.config,"logRollers")))
        # src/a8/launcher/Launcher.hx:353
        def _hx_local_1(i):
            # src/a8/launcher/Launcher.hx:353
            i.init()
        Lambda.iter(self.logRollers,_hx_local_1)

    def get_a8VersionsCache(self):
        # src/a8/launcher/Launcher.hx:27
        return tink_core__Lazy_Lazy_Impl_.get(self.lazy_a8VersionsCache)

    def get_installDir(self):
        # src/a8/launcher/Launcher.hx:30
        return tink_core__Lazy_Lazy_Impl_.get(self.lazy_installDir)

    def get_logsDir(self):
        # src/a8/launcher/Launcher.hx:31
        return tink_core__Lazy_Lazy_Impl_.get(self.lazy_logsDir)

    def get_logArchivesDir(self):
        # src/a8/launcher/Launcher.hx:32
        return tink_core__Lazy_Lazy_Impl_.get(self.lazy_logArchivesDir)

    @staticmethod
    def initDirectory(configEntry,secondEntry,basePath,makeDirectory = None):
        # src/a8/launcher/Launcher.hx:41
        entry = (configEntry if ((configEntry is not None)) else secondEntry)
        # src/a8/launcher/Launcher.hx:42
        d = None
        # src/a8/launcher/Launcher.hx:43
        if (entry is None):
            d = basePath
        else:
            # src/a8/launcher/Launcher.hx:46
            asPath = a8_PathOps.path(entry)
            # src/a8/launcher/Launcher.hx:42
            d = (asPath if (a8_PathOps.isAbsolute(asPath)) else a8_PathOps.entry(basePath,entry))
        # src/a8/launcher/Launcher.hx:53
        if (makeDirectory and (not a8_PathOps.exists(d))):
            a8_PathOps.makeDirectories(d)
        # src/a8/launcher/Launcher.hx:56
        return d

a8_launcher_Launcher._hx_class = a8_launcher_Launcher


class a8_launcher_LogRollerOps:
    _hx_class_name = "a8.launcher.LogRollerOps"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["fromConfig", "scheduleAtMidnight"]

    @staticmethod
    def fromConfig(c,launcher):
        # src/a8/launcher/LogRoller.hx:11
        if (c == "midnight"):
            return a8_launcher_MidnightLogRoller(launcher)
        else:
            return a8_launcher_UnknownLogRoller(c)

    @staticmethod
    def scheduleAtMidnight(fn):
        # src/a8/launcher/LogRoller.hx:18
        now = Date.now()
        # src/a8/launcher/LogRoller.hx:19
        midnight = a8_DateOps.midnight()
        # src/a8/launcher/LogRoller.hx:20
        millisToMidnight = ((midnight.date.timestamp() * 1000) - ((now.date.timestamp() * 1000)))
        # src/a8/launcher/LogRoller.hx:21
        secondsToMidnight = (millisToMidnight / 1000)
        # src/a8/launcher/LogRoller.hx:22
        a8_GlobalScheduler.schedule(secondsToMidnight,fn)
a8_launcher_LogRollerOps._hx_class = a8_launcher_LogRollerOps


class a8_launcher_LogRoller:
    _hx_class_name = "a8.launcher.LogRoller"
    _hx_is_interface = "True"
    __slots__ = ()
    _hx_methods = ["init", "onArchiveLogChanges"]
a8_launcher_LogRoller._hx_class = a8_launcher_LogRoller


class a8_launcher_AbstractLogRoller:
    _hx_class_name = "a8.launcher.AbstractLogRoller"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_methods = ["init", "onArchiveLogChanges"]

    def init(self):
        pass

    def onArchiveLogChanges(self):
        pass

a8_launcher_AbstractLogRoller._hx_class = a8_launcher_AbstractLogRoller


class a8_launcher_MidnightLogRoller(a8_launcher_AbstractLogRoller):
    _hx_class_name = "a8.launcher.MidnightLogRoller"
    _hx_is_interface = "False"
    __slots__ = ("launcher",)
    _hx_fields = ["launcher"]
    _hx_methods = ["init", "schedule", "doMidnightRollover"]
    _hx_statics = []
    _hx_interfaces = [a8_launcher_LogRoller]
    _hx_super = a8_launcher_AbstractLogRoller


    def __init__(self,launcher):
        # src/a8/launcher/LogRoller.hx:42
        self.launcher = launcher

    def init(self):
        # src/a8/launcher/LogRoller.hx:45
        self.schedule()

    def schedule(self):
        # src/a8/launcher/LogRoller.hx:49
        a8_launcher_LogRollerOps.scheduleAtMidnight(self.doMidnightRollover)

    def doMidnightRollover(self):
        # src/a8/launcher/LogRoller.hx:53
        self.launcher.logTrace("running doMidnightRollover",_hx_AnonObject({'fileName': "src/a8/launcher/LogRoller.hx", 'lineNumber': 53, 'className': "a8.launcher.MidnightLogRoller", 'methodName': "doMidnightRollover"}))
        # src/a8/launcher/LogRoller.hx:54
        timestampStr = a8_PathOps.timestampStr()
        # src/a8/launcher/LogRoller.hx:56
        self.launcher.pipedStderr.rollover(timestampStr)
        # src/a8/launcher/LogRoller.hx:57
        self.launcher.pipedStdout.rollover(timestampStr)
        # src/a8/launcher/LogRoller.hx:58
        self.schedule()
        # src/a8/launcher/LogRoller.hx:59
        self.launcher.logTrace("doMidnightRollover complete",_hx_AnonObject({'fileName': "src/a8/launcher/LogRoller.hx", 'lineNumber': 59, 'className': "a8.launcher.MidnightLogRoller", 'methodName': "doMidnightRollover"}))

a8_launcher_MidnightLogRoller._hx_class = a8_launcher_MidnightLogRoller


class a8_launcher_UnknownLogRoller(a8_launcher_AbstractLogRoller):
    _hx_class_name = "a8.launcher.UnknownLogRoller"
    _hx_is_interface = "False"
    __slots__ = ("config",)
    _hx_fields = ["config"]
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = [a8_launcher_LogRoller]
    _hx_super = a8_launcher_AbstractLogRoller


    def __init__(self,config):
        # src/a8/launcher/LogRoller.hx:67
        self.config = config

a8_launcher_UnknownLogRoller._hx_class = a8_launcher_UnknownLogRoller


class a8_launcher_CullOldArchivesLogRoller(a8_launcher_AbstractLogRoller):
    _hx_class_name = "a8.launcher.CullOldArchivesLogRoller"
    _hx_is_interface = "False"
    __slots__ = ("config", "launcher")
    _hx_fields = ["config", "launcher"]
    _hx_methods = ["init", "cullOldLogs"]
    _hx_statics = []
    _hx_interfaces = [a8_launcher_LogRoller]
    _hx_super = a8_launcher_AbstractLogRoller


    def __init__(self,config,launcher):
        # src/a8/launcher/LogRoller.hx:77
        self.config = config
        # src/a8/launcher/LogRoller.hx:78
        self.launcher = launcher

    def init(self):
        # src/a8/launcher/LogRoller.hx:84
        a8_GlobalScheduler.submit(self.cullOldLogs)

    def cullOldLogs(self):
        # src/a8/launcher/LogRoller.hx:89
        fiveMinutes = 300
        # src/a8/launcher/LogRoller.hx:90
        a8_GlobalScheduler.schedule(fiveMinutes,self.cullOldLogs)

a8_launcher_CullOldArchivesLogRoller._hx_class = a8_launcher_CullOldArchivesLogRoller


class a8_launcher_Main:
    _hx_class_name = "a8.launcher.Main"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["loadConfig", "helpString", "main"]

    @staticmethod
    def loadConfig():
        # src/a8/launcher/Main.hx:17
        execPath = a8_PathOps.executablePath()
        # src/a8/launcher/Main.hx:18
        appName = execPath.file
        # src/a8/launcher/Main.hx:20
        configExtensions = [".json", ".launcher.json"]
        # src/a8/launcher/Main.hx:23
        _g = []
        x = HxOverrides.iterator(a8_PathOps.symlinkChain(execPath))
        while x.hasNext():
            x1 = x.next()
            # src/a8/launcher/Main.hx:25
            l = [x1]
            def _hx_local_1(l):
                def _hx_local_0(e):
                    return a8_PathOps.entry(a8_PathOps.parent((l[0] if 0 < len(l) else None)),(HxOverrides.stringOrNull(a8_PathOps.name((l[0] if 0 < len(l) else None))) + ("null" if e is None else e)))
                return _hx_local_0
            # src/a8/launcher/Main.hx:23
            x2 = list(map(_hx_local_1(l),configExtensions))
            _g.append(x2)
        _g1 = []
        e = HxOverrides.iterator(_g)
        while e.hasNext():
            e1 = e.next()
            x = HxOverrides.iterator(e1)
            while x.hasNext():
                x1 = x.next()
                _g1.append(x1)
        # src/a8/launcher/Main.hx:22
        possibleConfigFiles = Lambda.array(_g1)
        # src/a8/launcher/Main.hx:33
        def _hx_local_2(f):
            # src/a8/launcher/Main.hx:33
            return a8_PathOps.exists(f)
        # src/a8/launcher/Main.hx:31
        configFile = Lambda.find(possibleConfigFiles,_hx_local_2)
        # src/a8/launcher/Main.hx:36
        config = python_lib_Json.loads(a8_PathOps.readText(configFile),**python__KwArgs_KwArgs_Impl_.fromT(_hx_AnonObject({'object_hook': python_Lib.dictToAnon})))
        # src/a8/launcher/Main.hx:38
        if (Reflect.field(config,"quiet") is None):
            Reflect.setField(config,"quiet",False)
        # src/a8/launcher/Main.hx:41
        if (Reflect.field(config,"logRollers") is None):
            Reflect.setField(config,"logRollers",[])
        # src/a8/launcher/Main.hx:44
        if (Reflect.field(config,"logFiles") is None):
            Reflect.setField(config,"logFiles",True)
        # src/a8/launcher/Main.hx:47
        if (config.kind == "jvm_cli"):
            # src/a8/launcher/Main.hx:48
            jvmLaunchConfig = config
            # src/a8/launcher/Main.hx:49
            Reflect.setField(config,"installDir",None)
            # src/a8/launcher/Main.hx:50
            Reflect.setField(config,"logFiles",False)
            # src/a8/launcher/Main.hx:51
            Reflect.setField(config,"logRollers",[])
        # src/a8/launcher/Main.hx:53
        if ((config.kind == "jvm") or ((config.kind == "jvm_cli"))):
            # src/a8/launcher/Main.hx:54
            jvmLaunchConfig = config
            # src/a8/launcher/Main.hx:55
            if (Reflect.field(jvmLaunchConfig,"jvmArgs") is None):
                Reflect.setField(jvmLaunchConfig,"jvmArgs",[])
            # src/a8/launcher/Main.hx:57
            if (Reflect.field(jvmLaunchConfig,"args") is None):
                Reflect.setField(jvmLaunchConfig,"args",[])
        # src/a8/launcher/Main.hx:62
        return config

    @staticmethod
    def helpString():
        # src/a8/launcher/Main.hx:69
        return "\nAccur8 Launcher Tool\n\n    The launchers job is to make sure the app is installed in the local cache and run the app it is configured to run.  \n\n    It will usually be installed (using Accur8 Recipes ie: a8-recipe install a8-scripts) at ~/tools-a8/packages/a8-scripts/a8-launcher.py\n\nConfiguration:\n    An app being run by the a8-launcher.py (or a copy/symbolic link of the launcher like a8-zoo) is configured by a .json file which will be alongside the command. \n    The base filename of the command needs to be the same as the json file. \n    So if you run the ‘a8-zoo’ launch command it will look for a ‘a8-zoo.json’ sitting alongside the a8-zoo command. \n    An example of a8-zoo.json will look like:\n        {\n            \"kind\": \"jvm_cli\",\n            \"mainClass\": \"a8.zoolander.Main\",\n            \"organization\": \"a8\",\n            \"artifact\": \"a8-zoolander_2.12\",\n            \"branch\": \"master\"\n        }\n\nUsage requirements:\n\n    Python 3.4+ (currently Python versions 3.7+ do not work)\n\n\nUsage:\n    --l-version <version> [<args>]\n        Runs the app with the specific version requested.\n\n    --l-resolveOnly\n        Does not run the app.\n        Sets up the inventory file(s) in a8VersionCache (~/a8/versions/cache) which contain app installer config and classpaths to jars.\n    \n    --l-help\n        Does not run the app.\n        Shows this help text.\n\n    [<args>]\n        Run the app passing through whatever arguments are passed in\n        \n"

    @staticmethod
    def main():
        # src/a8/launcher/Main.hx:114
        exitCode = 0
        # src/a8/launcher/Main.hx:116
        try:
            # src/a8/launcher/Main.hx:118
            execPath = a8_PathOps.executablePath()
            # src/a8/launcher/Main.hx:120
            appName = execPath.file
            # src/a8/launcher/Main.hx:122
            initialConfig = a8_launcher_Main.loadConfig()
            # src/a8/launcher/Main.hx:124
            args = list(python_lib_Sys.argv)
            # src/a8/launcher/Main.hx:125
            Reflect.setField(initialConfig,"rawCommandLineArgs",args)
            # src/a8/launcher/Main.hx:127
            clp = a8_launcher_CommandLineProcessor()
            # src/a8/launcher/Main.hx:128
            config = clp.apply(initialConfig)
            # src/a8/launcher/Main.hx:130
            a8_Logger.traceEnabled = (not Reflect.field(config,"quiet"))
            # src/a8/launcher/Main.hx:132
            if Reflect.field(config,"showHelp"):
                python_Lib.printString(Std.string(a8_launcher_Main.helpString()))
            else:
                # src/a8/launcher/Main.hx:135
                launcher = a8_launcher_Launcher(config,appName,args)
                # src/a8/launcher/Main.hx:141
                exitCode = launcher.runAndWait()
        except BaseException as _g:
            # ?:1
            None
            e = haxe_Exception.caught(_g).unwrap()
            # src/a8/launcher/Main.hx:144
            # src/a8/launcher/Main.hx:145
            stack = haxe__CallStack_CallStack_Impl_.exceptionStack()
            # src/a8/launcher/Main.hx:146
            a8_Logger.warn(((("" + Std.string(e)) + "\n") + HxOverrides.stringOrNull(a8_HaxeOps2.asString(stack,"    "))),_hx_AnonObject({'fileName': "src/a8/launcher/Main.hx", 'lineNumber': 146, 'className': "a8.launcher.Main", 'methodName': "main"}))
            # src/a8/launcher/Main.hx:147
            Sys.exit(1)
        # src/a8/launcher/Main.hx:150
        Sys.exit(exitCode)
a8_launcher_Main._hx_class = a8_launcher_Main


class a8_launcher_PipedStream:
    _hx_class_name = "a8.launcher.PipedStream"
    _hx_is_interface = "False"
    __slots__ = ("launcher", "processInput", "stdxxx", "fileExtension", "firstIO", "pipeToLogFiles", "initialTimestampStr", "pipe", "outputFile", "started")
    _hx_fields = ["launcher", "processInput", "stdxxx", "fileExtension", "firstIO", "pipeToLogFiles", "initialTimestampStr", "pipe", "outputFile", "started"]
    _hx_methods = ["start", "newOutputFile", "timestampedOutputFile", "log", "rollover", "close"]

    def __init__(self,launcher,processInput,stdxxx,fileExtension,firstIO,pipeToLogFiles,initialTimestampStr):
        # src/a8/launcher/PipedStream.hx:22
        self.pipe = None
        # src/a8/launcher/PipedStream.hx:26
        self.started = False
        # src/a8/launcher/PipedStream.hx:14
        self.launcher = launcher
        # src/a8/launcher/PipedStream.hx:15
        self.processInput = processInput
        # src/a8/launcher/PipedStream.hx:16
        self.stdxxx = stdxxx
        # src/a8/launcher/PipedStream.hx:17
        self.fileExtension = fileExtension
        # src/a8/launcher/PipedStream.hx:18
        self.firstIO = firstIO
        # src/a8/launcher/PipedStream.hx:19
        self.pipeToLogFiles = pipeToLogFiles
        # src/a8/launcher/PipedStream.hx:20
        self.initialTimestampStr = initialTimestampStr
        # src/a8/launcher/PipedStream.hx:24
        self.outputFile = haxe_ds_Option._hx_None

    def start(self):
        # src/a8/launcher/PipedStream.hx:29
        if (not self.started):
            # src/a8/launcher/PipedStream.hx:30
            self.started = True
            # src/a8/launcher/PipedStream.hx:31
            if self.pipeToLogFiles:
                # src/a8/launcher/PipedStream.hx:32
                of = self.newOutputFile(self.initialTimestampStr)
                # src/a8/launcher/PipedStream.hx:33
                self.outputFile = haxe_ds_Option.Some(of)
                # src/a8/launcher/PipedStream.hx:34
                self.pipe = a8_Pipe(self.processInput,of.teedOut,self.firstIO)
                # src/a8/launcher/PipedStream.hx:35
                self.pipe.run()
            else:
                # src/a8/launcher/PipedStream.hx:37
                self.outputFile = haxe_ds_Option._hx_None
                # src/a8/launcher/PipedStream.hx:38
                self.pipe = a8_Pipe(self.processInput,a8_StreamOps.asOutputStream(self.stdxxx),self.firstIO)
                # src/a8/launcher/PipedStream.hx:39
                self.pipe.run()

    def newOutputFile(self,timesatmpStr):
        # src/a8/launcher/PipedStream.hx:45
        fileOutputPath = self.timestampedOutputFile(timesatmpStr)
        # src/a8/launcher/PipedStream.hx:46
        fileOut = a8_StreamOps.fileOutputStream(a8_PathOps.realPathStr(fileOutputPath))
        # src/a8/launcher/PipedStream.hx:47
        teeOut = a8_TeeOutputStream([fileOut, a8_StreamOps.asOutputStream(self.stdxxx)])
        # src/a8/launcher/PipedStream.hx:48
        return _hx_AnonObject({'path': fileOutputPath, 'outputStream': fileOut, 'teedOut': teeOut})

    def timestampedOutputFile(self,timestampStr):
        # src/a8/launcher/PipedStream.hx:56
        return a8_PathOps.entry(self.launcher.get_logsDir(),((((HxOverrides.stringOrNull(self.launcher.appName) + ".") + ("null" if timestampStr is None else timestampStr)) + ".") + HxOverrides.stringOrNull(self.fileExtension)))

    def log(self,msg):
        # src/a8/launcher/PipedStream.hx:60
        _g = self.outputFile
        if (_g.index == 0):
            # src/a8/launcher/PipedStream.hx:61
            of = _g.params[0]
            # src/a8/launcher/PipedStream.hx:62
            try:
                # src/a8/launcher/PipedStream.hx:63
                of.teedOut.write(msg)
                # src/a8/launcher/PipedStream.hx:64
                of.teedOut.write("\n")
            except BaseException as _g:
                # ?:1
                None
                e = haxe_Exception.caught(_g).unwrap()
                # src/a8/launcher/PipedStream.hx:66
                a8_Logger.warn(("error logging - " + Std.string(e)),_hx_AnonObject({'fileName': "src/a8/launcher/PipedStream.hx", 'lineNumber': 66, 'className': "a8.launcher.PipedStream", 'methodName': "log"}))

    def rollover(self,timestampStr):
        # src/a8/launcher/PipedStream.hx:73
        _g = self.outputFile
        tmp = _g.index
        # src/a8/launcher/PipedStream.hx:74
        if (tmp == 0):
            # src/a8/launcher/PipedStream.hx:74
            existingOutputFile = _g.params[0]
            # src/a8/launcher/PipedStream.hx:77
            newFileOutputPath = self.timestampedOutputFile(timestampStr)
            # src/a8/launcher/PipedStream.hx:78
            newfileOut = a8_PathOps.outputStream(newFileOutputPath)
            # src/a8/launcher/PipedStream.hx:79
            def _hx_local_0(oldOut):
                # src/a8/launcher/PipedStream.hx:80
                oldOut.close()
                # src/a8/launcher/PipedStream.hx:81
                return newfileOut
            self.pipe.replaceOutput = _hx_local_0
            # src/a8/launcher/PipedStream.hx:85
            oldFileoutputPath = existingOutputFile.path
            # src/a8/launcher/PipedStream.hx:86
            existingOutputFile.path = newFileOutputPath
            # src/a8/launcher/PipedStream.hx:87
            existingOutputFile.outputStream = newfileOut
            # src/a8/launcher/PipedStream.hx:88
            self.launcher.archiveLogFiles([oldFileoutputPath])
        elif (tmp == 1):
            raise haxe_Exception.thrown(a8_Exception("this should not happen since rollover should never get called when we don't have a Some for outputFile: Option<PipedStreamOutputFile>",None,_hx_AnonObject({'fileName': "src/a8/launcher/PipedStream.hx", 'lineNumber': 92, 'className': "a8.launcher.PipedStream", 'methodName': "rollover"})))
        else:
            pass

    def close(self):
        # src/a8/launcher/PipedStream.hx:98
        def _hx_local_0(f):
            # src/a8/launcher/PipedStream.hx:98
            f.teedOut.close()
        a8_OptionOps.iter(self.outputFile,_hx_local_0)

a8_launcher_PipedStream._hx_class = a8_launcher_PipedStream

class haxe_StackItem(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.StackItem"
    _hx_constructs = ["CFunction", "Module", "FilePos", "Method", "LocalFunction"]

    @staticmethod
    def Module(m):
        return haxe_StackItem("Module", 1, (m,))

    @staticmethod
    def FilePos(s,file,line,column = None):
        return haxe_StackItem("FilePos", 2, (s,file,line,column))

    @staticmethod
    def Method(classname,method):
        return haxe_StackItem("Method", 3, (classname,method))

    @staticmethod
    def LocalFunction(v = None):
        return haxe_StackItem("LocalFunction", 4, (v,))
haxe_StackItem.CFunction = haxe_StackItem("CFunction", 0, ())
haxe_StackItem._hx_class = haxe_StackItem


class haxe__CallStack_CallStack_Impl_:
    _hx_class_name = "haxe._CallStack.CallStack_Impl_"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["callStack", "exceptionStack", "subtract", "equalItems"]

    @staticmethod
    def callStack():
        # /Users/glen/bin/haxe-4.2.5/std/haxe/CallStack.hx:52
        infos = python_lib_Traceback.extract_stack()
        if (len(infos) != 0):
            infos.pop()
        infos.reverse()
        return haxe_NativeStackTrace.toHaxe(infos)

    @staticmethod
    def exceptionStack(fullStack = None):
        # /Users/glen/bin/haxe-4.2.5/std/haxe/CallStack.hx:63
        if (fullStack is None):
            fullStack = False
        # /Users/glen/bin/haxe-4.2.5/std/haxe/CallStack.hx:64
        eStack = haxe_NativeStackTrace.toHaxe(haxe_NativeStackTrace.exceptionStack())
        # /Users/glen/bin/haxe-4.2.5/std/haxe/CallStack.hx:65
        return (eStack if fullStack else haxe__CallStack_CallStack_Impl_.subtract(eStack,haxe__CallStack_CallStack_Impl_.callStack()))

    @staticmethod
    def subtract(this1,stack):
        # /Users/glen/bin/haxe-4.2.5/std/haxe/CallStack.hx:85
        startIndex = -1
        # /Users/glen/bin/haxe-4.2.5/std/haxe/CallStack.hx:86
        i = -1
        # /Users/glen/bin/haxe-4.2.5/std/haxe/CallStack.hx:87
        while True:
            # /Users/glen/bin/haxe-4.2.5/std/haxe/CallStack.hx:87
            i = (i + 1)
            tmp = i
            if (not ((tmp < len(this1)))):
                break
            # /Users/glen/bin/haxe-4.2.5/std/haxe/CallStack.hx:88
            # /Users/glen/bin/haxe-4.2.5/std/haxe/CallStack.hx:88
            _g = 0
            _g1 = len(stack)
            while (_g < _g1):
                j = _g
                _g = (_g + 1)
                # /Users/glen/bin/haxe-4.2.5/std/haxe/CallStack.hx:89
                if haxe__CallStack_CallStack_Impl_.equalItems((this1[i] if i >= 0 and i < len(this1) else None),python_internal_ArrayImpl._get(stack, j)):
                    # /Users/glen/bin/haxe-4.2.5/std/haxe/CallStack.hx:90
                    if (startIndex < 0):
                        startIndex = i
                    # /Users/glen/bin/haxe-4.2.5/std/haxe/CallStack.hx:93
                    i = (i + 1)
                    # /Users/glen/bin/haxe-4.2.5/std/haxe/CallStack.hx:94
                    if (i >= len(this1)):
                        break
                else:
                    startIndex = -1
            # /Users/glen/bin/haxe-4.2.5/std/haxe/CallStack.hx:99
            if (startIndex >= 0):
                break
        # /Users/glen/bin/haxe-4.2.5/std/haxe/CallStack.hx:101
        if (startIndex >= 0):
            return this1[0:startIndex]
        else:
            return this1

    @staticmethod
    def equalItems(item1,item2):
        # /Users/glen/bin/haxe-4.2.5/std/haxe/CallStack.hx:120
        if (item1 is None):
            if (item2 is None):
                return True
            else:
                return False
        else:
            # /Users/glen/bin/haxe-4.2.5/std/haxe/CallStack.hx:120
            tmp = item1.index
            if (tmp == 0):
                if (item2 is None):
                    return False
                elif (item2.index == 0):
                    return True
                else:
                    return False
            elif (tmp == 1):
                if (item2 is None):
                    return False
                elif (item2.index == 1):
                    # /Users/glen/bin/haxe-4.2.5/std/haxe/CallStack.hx:123
                    m2 = item2.params[0]
                    m1 = item1.params[0]
                    # /Users/glen/bin/haxe-4.2.5/std/haxe/CallStack.hx:124
                    return (m1 == m2)
                else:
                    return False
            elif (tmp == 2):
                if (item2 is None):
                    return False
                elif (item2.index == 2):
                    # /Users/glen/bin/haxe-4.2.5/std/haxe/CallStack.hx:125
                    item21 = item2.params[0]
                    file2 = item2.params[1]
                    line2 = item2.params[2]
                    col2 = item2.params[3]
                    col1 = item1.params[3]
                    line1 = item1.params[2]
                    file1 = item1.params[1]
                    item11 = item1.params[0]
                    # /Users/glen/bin/haxe-4.2.5/std/haxe/CallStack.hx:126
                    if (((file1 == file2) and ((line1 == line2))) and ((col1 == col2))):
                        return haxe__CallStack_CallStack_Impl_.equalItems(item11,item21)
                    else:
                        return False
                else:
                    return False
            elif (tmp == 3):
                if (item2 is None):
                    return False
                elif (item2.index == 3):
                    # /Users/glen/bin/haxe-4.2.5/std/haxe/CallStack.hx:127
                    class2 = item2.params[0]
                    method2 = item2.params[1]
                    method1 = item1.params[1]
                    class1 = item1.params[0]
                    # /Users/glen/bin/haxe-4.2.5/std/haxe/CallStack.hx:128
                    if (class1 == class2):
                        return (method1 == method2)
                    else:
                        return False
                else:
                    return False
            elif (tmp == 4):
                if (item2 is None):
                    return False
                elif (item2.index == 4):
                    # /Users/glen/bin/haxe-4.2.5/std/haxe/CallStack.hx:129
                    v2 = item2.params[0]
                    v1 = item1.params[0]
                    # /Users/glen/bin/haxe-4.2.5/std/haxe/CallStack.hx:130
                    return (v1 == v2)
                else:
                    return False
            else:
                pass
haxe__CallStack_CallStack_Impl_._hx_class = haxe__CallStack_CallStack_Impl_


class haxe_Exception(Exception):
    _hx_class_name = "haxe.Exception"
    _hx_is_interface = "False"
    __slots__ = ("_hx___nativeStack", "_hx___skipStack", "_hx___nativeException", "_hx___previousException")
    _hx_fields = ["__nativeStack", "__skipStack", "__nativeException", "__previousException"]
    _hx_methods = ["unwrap", "toString", "get_message", "get_native"]
    _hx_statics = ["caught", "thrown"]
    _hx_interfaces = []
    _hx_super = Exception


    def __init__(self,message,previous = None,native = None):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/haxe/Exception.hx:21
        self._hx___previousException = None
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/haxe/Exception.hx:20
        self._hx___nativeException = None
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/haxe/Exception.hx:18
        self._hx___nativeStack = None
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/haxe/Exception.hx:19
        self._hx___skipStack = 0
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/haxe/Exception.hx:46
        super().__init__(message)
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/haxe/Exception.hx:47
        self._hx___previousException = previous
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/haxe/Exception.hx:48
        if ((native is not None) and Std.isOfType(native,BaseException)):
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/haxe/Exception.hx:49
            self._hx___nativeException = native
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/haxe/Exception.hx:50
            self._hx___nativeStack = haxe_NativeStackTrace.exceptionStack()
        else:
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/haxe/Exception.hx:52
            self._hx___nativeException = self
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/haxe/Exception.hx:53
            infos = python_lib_Traceback.extract_stack()
            if (len(infos) != 0):
                infos.pop()
            infos.reverse()
            self._hx___nativeStack = infos

    def unwrap(self):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/haxe/Exception.hx:58
        return self._hx___nativeException

    def toString(self):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/haxe/Exception.hx:62
        return self.get_message()

    def get_message(self):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/haxe/Exception.hx:76
        return str(self)

    def get_native(self):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/haxe/Exception.hx:84
        return self._hx___nativeException

    @staticmethod
    def caught(value):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/haxe/Exception.hx:24
        if Std.isOfType(value,haxe_Exception):
            return value
        elif Std.isOfType(value,BaseException):
            return haxe_Exception(str(value),None,value)
        else:
            return haxe_ValueException(value,None,value)

    @staticmethod
    def thrown(value):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/haxe/Exception.hx:34
        if Std.isOfType(value,haxe_Exception):
            return value.get_native()
        elif Std.isOfType(value,BaseException):
            return value
        else:
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/haxe/Exception.hx:39
            e = haxe_ValueException(value)
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/haxe/Exception.hx:40
            e._hx___skipStack = (e._hx___skipStack + 1)
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/haxe/Exception.hx:41
            return e

haxe_Exception._hx_class = haxe_Exception


class haxe_Log:
    _hx_class_name = "haxe.Log"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["formatOutput", "trace"]

    @staticmethod
    def formatOutput(v,infos):
        # /Users/glen/bin/haxe-4.2.5/std/haxe/Log.hx:34
        _hx_str = Std.string(v)
        # /Users/glen/bin/haxe-4.2.5/std/haxe/Log.hx:35
        if (infos is None):
            return _hx_str
        # /Users/glen/bin/haxe-4.2.5/std/haxe/Log.hx:37
        pstr = ((HxOverrides.stringOrNull(infos.fileName) + ":") + Std.string(infos.lineNumber))
        # /Users/glen/bin/haxe-4.2.5/std/haxe/Log.hx:38
        if (Reflect.field(infos,"customParams") is not None):
            # /Users/glen/bin/haxe-4.2.5/std/haxe/Log.hx:39
            _g = 0
            _g1 = Reflect.field(infos,"customParams")
            while (_g < len(_g1)):
                v = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
                _g = (_g + 1)
                # /Users/glen/bin/haxe-4.2.5/std/haxe/Log.hx:40
                _hx_str = (("null" if _hx_str is None else _hx_str) + ((", " + Std.string(v))))
        # /Users/glen/bin/haxe-4.2.5/std/haxe/Log.hx:41
        return ((("null" if pstr is None else pstr) + ": ") + ("null" if _hx_str is None else _hx_str))

    @staticmethod
    def trace(v,infos = None):
        # /Users/glen/bin/haxe-4.2.5/std/haxe/Log.hx:63
        _hx_str = haxe_Log.formatOutput(v,infos)
        # /Users/glen/bin/haxe-4.2.5/std/haxe/Log.hx:70
        # /Users/glen/bin/haxe-4.2.5/std/haxe/Log.hx:70
        str1 = Std.string(_hx_str)
        python_Lib.printString((("" + ("null" if str1 is None else str1)) + HxOverrides.stringOrNull(python_Lib.lineEnd)))
haxe_Log._hx_class = haxe_Log


class haxe_NativeStackTrace:
    _hx_class_name = "haxe.NativeStackTrace"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["saveStack", "exceptionStack", "toHaxe"]

    @staticmethod
    def saveStack(exception):
        pass

    @staticmethod
    def exceptionStack():
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/haxe/NativeStackTrace.hx:25
        exc = python_lib_Sys.exc_info()
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/haxe/NativeStackTrace.hx:26
        if (exc[2] is not None):
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/haxe/NativeStackTrace.hx:27
            infos = python_lib_Traceback.extract_tb(exc[2])
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/haxe/NativeStackTrace.hx:28
            infos.reverse()
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/haxe/NativeStackTrace.hx:29
            return infos
        else:
            return []

    @staticmethod
    def toHaxe(native,skip = None):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/haxe/NativeStackTrace.hx:35
        if (skip is None):
            skip = 0
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/haxe/NativeStackTrace.hx:36
        stack = []
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/haxe/NativeStackTrace.hx:37
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/haxe/NativeStackTrace.hx:37
        _g = 0
        _g1 = len(native)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/haxe/NativeStackTrace.hx:38
            if (skip > i):
                continue
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/haxe/NativeStackTrace.hx:41
            elem = (native[i] if i >= 0 and i < len(native) else None)
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/haxe/NativeStackTrace.hx:42
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/haxe/NativeStackTrace.hx:42
            x = haxe_StackItem.FilePos(haxe_StackItem.Method(None,elem[2]),elem[0],elem[1])
            stack.append(x)
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/haxe/NativeStackTrace.hx:44
        return stack
haxe_NativeStackTrace._hx_class = haxe_NativeStackTrace


class haxe_Timer:
    _hx_class_name = "haxe.Timer"
    _hx_is_interface = "False"
    _hx_fields = ["thread", "eventHandler"]
    _hx_methods = ["stop", "run"]
    _hx_statics = ["delay"]

    def __init__(self,time_ms):
        # /Users/glen/bin/haxe-4.2.5/std/haxe/Timer.hx:49
        self.eventHandler = None
        # /Users/glen/bin/haxe-4.2.5/std/haxe/Timer.hx:48
        self.thread = None
        # /Users/glen/bin/haxe-4.2.5/std/haxe/Timer.hx:65
        _gthis = self
        # /Users/glen/bin/haxe-4.2.5/std/haxe/Timer.hx:75
        self.thread = sys_thread__Thread_HxThread.current()
        # /Users/glen/bin/haxe-4.2.5/std/haxe/Timer.hx:76
        def _hx_local_0():
            # /Users/glen/bin/haxe-4.2.5/std/haxe/Timer.hx:76
            _gthis.run()
        self.eventHandler = sys_thread__Thread_Thread_Impl_.get_events(self.thread).repeat(_hx_local_0,time_ms)

    def stop(self):
        # /Users/glen/bin/haxe-4.2.5/std/haxe/Timer.hx:106
        sys_thread__Thread_Thread_Impl_.get_events(self.thread).cancel(self.eventHandler)

    def run(self):
        pass

    @staticmethod
    def delay(f,time_ms):
        # /Users/glen/bin/haxe-4.2.5/std/haxe/Timer.hx:141
        t = haxe_Timer(time_ms)
        # /Users/glen/bin/haxe-4.2.5/std/haxe/Timer.hx:142
        def _hx_local_0():
            # /Users/glen/bin/haxe-4.2.5/std/haxe/Timer.hx:143
            t.stop()
            # /Users/glen/bin/haxe-4.2.5/std/haxe/Timer.hx:144
            f()
        t.run = _hx_local_0
        # /Users/glen/bin/haxe-4.2.5/std/haxe/Timer.hx:146
        return t

haxe_Timer._hx_class = haxe_Timer


class haxe_ValueException(haxe_Exception):
    _hx_class_name = "haxe.ValueException"
    _hx_is_interface = "False"
    __slots__ = ("value",)
    _hx_fields = ["value"]
    _hx_methods = ["unwrap"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_Exception


    def __init__(self,value,previous = None,native = None):
        # /Users/glen/bin/haxe-4.2.5/std/haxe/ValueException.hx:21
        self.value = None
        # /Users/glen/bin/haxe-4.2.5/std/haxe/ValueException.hx:24
        super().__init__(Std.string(value),previous,native)
        # /Users/glen/bin/haxe-4.2.5/std/haxe/ValueException.hx:25
        self.value = value

    def unwrap(self):
        # /Users/glen/bin/haxe-4.2.5/std/haxe/ValueException.hx:36
        return self.value

haxe_ValueException._hx_class = haxe_ValueException

class haxe_ds_Either(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.ds.Either"
    _hx_constructs = ["Left", "Right"]

    @staticmethod
    def Left(v):
        return haxe_ds_Either("Left", 0, (v,))

    @staticmethod
    def Right(v):
        return haxe_ds_Either("Right", 1, (v,))
haxe_ds_Either._hx_class = haxe_ds_Either


class haxe_ds_ObjectMap:
    _hx_class_name = "haxe.ds.ObjectMap"
    _hx_is_interface = "False"
    __slots__ = ("h",)
    _hx_fields = ["h"]
    _hx_methods = ["set", "get", "keys"]
    _hx_interfaces = [haxe_IMap]

    def __init__(self):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/haxe/ds/ObjectMap.hx:31
        self.h = dict()

    def set(self,key,value):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/haxe/ds/ObjectMap.hx:35
        self.h[key] = value

    def get(self,key):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/haxe/ds/ObjectMap.hx:39
        return self.h.get(key,None)

    def keys(self):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/haxe/ds/ObjectMap.hx:54
        return python_HaxeIterator(iter(self.h.keys()))

haxe_ds_ObjectMap._hx_class = haxe_ds_ObjectMap


class haxe_exceptions_PosException(haxe_Exception):
    _hx_class_name = "haxe.exceptions.PosException"
    _hx_is_interface = "False"
    __slots__ = ("posInfos",)
    _hx_fields = ["posInfos"]
    _hx_methods = ["toString"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_Exception


    def __init__(self,message,previous = None,pos = None):
        # /Users/glen/bin/haxe-4.2.5/std/haxe/exceptions/PosException.hx:10
        self.posInfos = None
        # /Users/glen/bin/haxe-4.2.5/std/haxe/exceptions/PosException.hx:13
        super().__init__(message,previous)
        # /Users/glen/bin/haxe-4.2.5/std/haxe/exceptions/PosException.hx:14
        if (pos is None):
            self.posInfos = _hx_AnonObject({'fileName': "(unknown)", 'lineNumber': 0, 'className': "(unknown)", 'methodName': "(unknown)"})
        else:
            self.posInfos = pos

    def toString(self):
        # /Users/glen/bin/haxe-4.2.5/std/haxe/exceptions/PosException.hx:25
        return ((((((((("" + HxOverrides.stringOrNull(super().toString())) + " in ") + HxOverrides.stringOrNull(self.posInfos.className)) + ".") + HxOverrides.stringOrNull(self.posInfos.methodName)) + " at ") + HxOverrides.stringOrNull(self.posInfos.fileName)) + ":") + Std.string(self.posInfos.lineNumber))

haxe_exceptions_PosException._hx_class = haxe_exceptions_PosException


class haxe_exceptions_NotImplementedException(haxe_exceptions_PosException):
    _hx_class_name = "haxe.exceptions.NotImplementedException"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_exceptions_PosException


    def __init__(self,message = None,previous = None,pos = None):
        # /Users/glen/bin/haxe-4.2.5/std/haxe/exceptions/NotImplementedException.hx:7
        if (message is None):
            message = "Not implemented"
        # /Users/glen/bin/haxe-4.2.5/std/haxe/exceptions/NotImplementedException.hx:8
        super().__init__(message,previous,pos)
haxe_exceptions_NotImplementedException._hx_class = haxe_exceptions_NotImplementedException


class haxe_format_JsonPrinter:
    _hx_class_name = "haxe.format.JsonPrinter"
    _hx_is_interface = "False"
    __slots__ = ("buf", "replacer", "indent", "pretty", "nind")
    _hx_fields = ["buf", "replacer", "indent", "pretty", "nind"]
    _hx_methods = ["write", "classString", "fieldsString", "quote"]
    _hx_statics = ["print"]

    def __init__(self,replacer,space):
        # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:57
        self.replacer = replacer
        # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:58
        self.indent = space
        # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:59
        self.pretty = (space is not None)
        # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:60
        self.nind = 0
        # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:67
        self.buf = StringBuf()

    def write(self,k,v):
        # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:82
        if (self.replacer is not None):
            v = self.replacer(k,v)
        # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:84
        # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:84
        _g = Type.typeof(v)
        tmp = _g.index
        # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:136
        if (tmp == 0):
            self.buf.b.write("null")
        elif (tmp == 1):
            # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:90
            _this = self.buf
            s = Std.string(v)
            _this.b.write(s)
        elif (tmp == 2):
            # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:92
            f = v
            v1 = (Std.string(v) if ((((f != Math.POSITIVE_INFINITY) and ((f != Math.NEGATIVE_INFINITY))) and (not python_lib_Math.isnan(f)))) else "null")
            _this = self.buf
            s = Std.string(v1)
            _this.b.write(s)
        elif (tmp == 3):
            # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:134
            _this = self.buf
            s = Std.string(v)
            _this.b.write(s)
        elif (tmp == 4):
            self.fieldsString(v,python_Boot.fields(v))
        elif (tmp == 5):
            self.buf.b.write("\"<fun>\"")
        elif (tmp == 6):
            # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:95
            c = _g.params[0]
            # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:96
            if (c == str):
                self.quote(v)
            elif (c == list):
                # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:99
                v1 = v
                # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:100
                # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:100
                _this = self.buf
                s = "".join(map(chr,[91]))
                _this.b.write(s)
                # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:102
                _hx_len = len(v1)
                # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:103
                last = (_hx_len - 1)
                # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:104
                # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:104
                _g1 = 0
                _g2 = _hx_len
                while (_g1 < _g2):
                    i = _g1
                    _g1 = (_g1 + 1)
                    # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:105
                    if (i > 0):
                        # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:106
                        _this = self.buf
                        s = "".join(map(chr,[44]))
                        _this.b.write(s)
                    else:
                        # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:108
                        _hx_local_0 = self
                        _hx_local_1 = _hx_local_0.nind
                        _hx_local_0.nind = (_hx_local_1 + 1)
                        _hx_local_1
                    # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:109
                    if self.pretty:
                        # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:109
                        _this1 = self.buf
                        s1 = "".join(map(chr,[10]))
                        _this1.b.write(s1)
                    # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:110
                    if self.pretty:
                        # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:110
                        v2 = StringTools.lpad("",self.indent,(self.nind * len(self.indent)))
                        _this2 = self.buf
                        s2 = Std.string(v2)
                        _this2.b.write(s2)
                    # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:111
                    self.write(i,(v1[i] if i >= 0 and i < len(v1) else None))
                    # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:112
                    if (i == last):
                        # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:113
                        # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:113
                        _hx_local_2 = self
                        _hx_local_3 = _hx_local_2.nind
                        _hx_local_2.nind = (_hx_local_3 - 1)
                        _hx_local_3
                        # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:114
                        if self.pretty:
                            # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:114
                            _this3 = self.buf
                            s3 = "".join(map(chr,[10]))
                            _this3.b.write(s3)
                        # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:115
                        if self.pretty:
                            # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:115
                            v3 = StringTools.lpad("",self.indent,(self.nind * len(self.indent)))
                            _this4 = self.buf
                            s4 = Std.string(v3)
                            _this4.b.write(s4)
                # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:118
                # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:118
                _this = self.buf
                s = "".join(map(chr,[93]))
                _this.b.write(s)
            elif (c == haxe_ds_StringMap):
                # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:120
                v1 = v
                # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:121
                o = _hx_AnonObject({})
                # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:122
                # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:122
                k = v1.keys()
                while k.hasNext():
                    k1 = k.next()
                    # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:123
                    # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:123
                    value = v1.h.get(k1,None)
                    setattr(o,(("_hx_" + k1) if ((k1 in python_Boot.keywords)) else (("_hx_" + k1) if (((((len(k1) > 2) and ((ord(k1[0]) == 95))) and ((ord(k1[1]) == 95))) and ((ord(k1[(len(k1) - 1)]) != 95)))) else k1)),value)
                # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:124
                # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:124
                v1 = o
                self.fieldsString(v1,python_Boot.fields(v1))
            elif (c == Date):
                # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:126
                v1 = v
                # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:127
                self.quote(v1.toString())
            else:
                self.classString(v)
        elif (tmp == 7):
            # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:130
            _g1 = _g.params[0]
            # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:131
            i = v.index
            # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:132
            # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:132
            _this = self.buf
            s = Std.string(i)
            _this.b.write(s)
        elif (tmp == 8):
            self.buf.b.write("\"???\"")
        else:
            pass

    def classString(self,v):
        # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:158
        self.fieldsString(v,python_Boot.getInstanceFields(Type.getClass(v)))

    def fieldsString(self,v,fields):
        # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:166
        # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:166
        _this = self.buf
        s = "".join(map(chr,[123]))
        _this.b.write(s)
        # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:167
        _hx_len = len(fields)
        # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:168
        last = (_hx_len - 1)
        # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:169
        first = True
        # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:170
        # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:170
        _g = 0
        _g1 = _hx_len
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:171
            f = (fields[i] if i >= 0 and i < len(fields) else None)
            # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:172
            value = Reflect.field(v,f)
            # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:173
            if Reflect.isFunction(value):
                continue
            # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:175
            if first:
                # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:176
                # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:176
                _hx_local_0 = self
                _hx_local_1 = _hx_local_0.nind
                _hx_local_0.nind = (_hx_local_1 + 1)
                _hx_local_1
                # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:177
                first = False
            else:
                # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:179
                _this = self.buf
                s = "".join(map(chr,[44]))
                _this.b.write(s)
            # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:180
            if self.pretty:
                # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:180
                _this1 = self.buf
                s1 = "".join(map(chr,[10]))
                _this1.b.write(s1)
            # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:181
            if self.pretty:
                # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:181
                v1 = StringTools.lpad("",self.indent,(self.nind * len(self.indent)))
                _this2 = self.buf
                s2 = Std.string(v1)
                _this2.b.write(s2)
            # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:182
            self.quote(f)
            # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:183
            # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:183
            _this3 = self.buf
            s3 = "".join(map(chr,[58]))
            _this3.b.write(s3)
            # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:184
            if self.pretty:
                # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:185
                _this4 = self.buf
                s4 = "".join(map(chr,[32]))
                _this4.b.write(s4)
            # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:186
            self.write(f,value)
            # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:187
            if (i == last):
                # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:188
                # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:188
                _hx_local_2 = self
                _hx_local_3 = _hx_local_2.nind
                _hx_local_2.nind = (_hx_local_3 - 1)
                _hx_local_3
                # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:189
                if self.pretty:
                    # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:189
                    _this5 = self.buf
                    s5 = "".join(map(chr,[10]))
                    _this5.b.write(s5)
                # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:190
                if self.pretty:
                    # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:190
                    v2 = StringTools.lpad("",self.indent,(self.nind * len(self.indent)))
                    _this6 = self.buf
                    s6 = Std.string(v2)
                    _this6.b.write(s6)
        # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:193
        # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:193
        _this = self.buf
        s = "".join(map(chr,[125]))
        _this.b.write(s)

    def quote(self,s):
        # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:203
        # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:203
        _this = self.buf
        s1 = "".join(map(chr,[34]))
        _this.b.write(s1)
        # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:204
        i = 0
        # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:205
        length = len(s)
        # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:209
        while (i < length):
            # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:210
            index = i
            i = (i + 1)
            c = ord(s[index])
            # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:211
            c1 = c
            # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:223
            if (c1 == 8):
                self.buf.b.write("\\b")
            elif (c1 == 9):
                self.buf.b.write("\\t")
            elif (c1 == 10):
                self.buf.b.write("\\n")
            elif (c1 == 12):
                self.buf.b.write("\\f")
            elif (c1 == 13):
                self.buf.b.write("\\r")
            elif (c1 == 34):
                self.buf.b.write("\\\"")
            elif (c1 == 92):
                self.buf.b.write("\\\\")
            else:
                # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:248
                _this = self.buf
                s1 = "".join(map(chr,[c]))
                _this.b.write(s1)
        # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:256
        # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:256
        _this = self.buf
        s = "".join(map(chr,[34]))
        _this.b.write(s)

    @staticmethod
    def print(o,replacer = None,space = None):
        # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:45
        printer = haxe_format_JsonPrinter(replacer,space)
        # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:46
        printer.write("",o)
        # /Users/glen/bin/haxe-4.2.5/std/haxe/format/JsonPrinter.hx:47
        return printer.buf.b.getvalue()

haxe_format_JsonPrinter._hx_class = haxe_format_JsonPrinter


class haxe_http_HttpBase:
    _hx_class_name = "haxe.http.HttpBase"
    _hx_is_interface = "False"
    _hx_fields = ["url", "responseBytes", "responseAsString", "postData", "postBytes", "headers", "params", "emptyOnData"]
    _hx_methods = ["onData", "onBytes", "onError", "onStatus", "hasOnData", "success", "get_responseData"]

    def __init__(self,url):
        # /Users/glen/bin/haxe-4.2.5/std/haxe/http/HttpBase.hx:58
        self.emptyOnData = None
        # /Users/glen/bin/haxe-4.2.5/std/haxe/http/HttpBase.hx:54
        self.postBytes = None
        # /Users/glen/bin/haxe-4.2.5/std/haxe/http/HttpBase.hx:53
        self.postData = None
        # /Users/glen/bin/haxe-4.2.5/std/haxe/http/HttpBase.hx:52
        self.responseAsString = None
        # /Users/glen/bin/haxe-4.2.5/std/haxe/http/HttpBase.hx:50
        self.responseBytes = None
        # /Users/glen/bin/haxe-4.2.5/std/haxe/http/HttpBase.hx:72
        self.url = url
        # /Users/glen/bin/haxe-4.2.5/std/haxe/http/HttpBase.hx:73
        self.headers = []
        # /Users/glen/bin/haxe-4.2.5/std/haxe/http/HttpBase.hx:74
        self.params = []
        # /Users/glen/bin/haxe-4.2.5/std/haxe/http/HttpBase.hx:75
        self.emptyOnData = self.onData

    def onData(self,data):
        pass

    def onBytes(self,data):
        pass

    def onError(self,msg):
        pass

    def onStatus(self,status):
        pass

    def hasOnData(self):
        # /Users/glen/bin/haxe-4.2.5/std/haxe/http/HttpBase.hx:229
        return (not Reflect.compareMethods(self.onData,self.emptyOnData))

    def success(self,data):
        # /Users/glen/bin/haxe-4.2.5/std/haxe/http/HttpBase.hx:233
        self.responseBytes = data
        # /Users/glen/bin/haxe-4.2.5/std/haxe/http/HttpBase.hx:234
        self.responseAsString = None
        # /Users/glen/bin/haxe-4.2.5/std/haxe/http/HttpBase.hx:235
        if self.hasOnData():
            self.onData(self.get_responseData())
        # /Users/glen/bin/haxe-4.2.5/std/haxe/http/HttpBase.hx:238
        self.onBytes(self.responseBytes)

    def get_responseData(self):
        # /Users/glen/bin/haxe-4.2.5/std/haxe/http/HttpBase.hx:242
        if ((self.responseAsString is None) and ((self.responseBytes is not None))):
            self.responseAsString = self.responseBytes.getString(0,self.responseBytes.length,haxe_io_Encoding.UTF8)
        # /Users/glen/bin/haxe-4.2.5/std/haxe/http/HttpBase.hx:249
        return self.responseAsString

haxe_http_HttpBase._hx_class = haxe_http_HttpBase


class haxe_io_Bytes:
    _hx_class_name = "haxe.io.Bytes"
    _hx_is_interface = "False"
    __slots__ = ("length", "b")
    _hx_fields = ["length", "b"]
    _hx_methods = ["sub", "getString", "toString"]
    _hx_statics = ["alloc", "ofString", "ofData"]

    def __init__(self,length,b):
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Bytes.hx:35
        self.length = length
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Bytes.hx:36
        self.b = b

    def sub(self,pos,_hx_len):
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Bytes.hx:157
        if (((pos < 0) or ((_hx_len < 0))) or (((pos + _hx_len) > self.length))):
            raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Bytes.hx:176
        return haxe_io_Bytes(_hx_len,self.b[pos:(pos + _hx_len)])

    def getString(self,pos,_hx_len,encoding = None):
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Bytes.hx:416
        tmp = (encoding is None)
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Bytes.hx:419
        if (((pos < 0) or ((_hx_len < 0))) or (((pos + _hx_len) > self.length))):
            raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Bytes.hx:450
        return self.b[pos:pos+_hx_len].decode('UTF-8','replace')

    def toString(self):
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Bytes.hx:516
        return self.getString(0,self.length)

    @staticmethod
    def alloc(length):
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Bytes.hx:566
        return haxe_io_Bytes(length,bytearray(length))

    @staticmethod
    def ofString(s,encoding = None):
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Bytes.hx:615
        b = bytearray(s,"UTF-8")
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Bytes.hx:616
        return haxe_io_Bytes(len(b),b)

    @staticmethod
    def ofData(b):
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Bytes.hx:664
        return haxe_io_Bytes(len(b),b)

haxe_io_Bytes._hx_class = haxe_io_Bytes


class haxe_io_BytesBuffer:
    _hx_class_name = "haxe.io.BytesBuffer"
    _hx_is_interface = "False"
    __slots__ = ("b",)
    _hx_fields = ["b"]
    _hx_methods = ["getBytes"]

    def __init__(self):
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/BytesBuffer.hx:58
        self.b = bytearray()

    def getBytes(self):
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/BytesBuffer.hx:216
        _hx_bytes = haxe_io_Bytes(len(self.b),self.b)
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/BytesBuffer.hx:222
        self.b = None
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/BytesBuffer.hx:223
        return _hx_bytes

haxe_io_BytesBuffer._hx_class = haxe_io_BytesBuffer


class haxe_io_Output:
    _hx_class_name = "haxe.io.Output"
    _hx_is_interface = "False"
    __slots__ = ("bigEndian",)
    _hx_fields = ["bigEndian"]
    _hx_methods = ["writeByte", "writeBytes", "flush", "close", "set_bigEndian", "writeFullBytes", "prepare", "writeString"]

    def writeByte(self,c):
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Output.hx:47
        raise haxe_exceptions_NotImplementedException(None,None,_hx_AnonObject({'fileName': "haxe/io/Output.hx", 'lineNumber': 47, 'className': "haxe.io.Output", 'methodName': "writeByte"}))

    def writeBytes(self,s,pos,_hx_len):
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Output.hx:59
        if (((pos < 0) or ((_hx_len < 0))) or (((pos + _hx_len) > s.length))):
            raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Output.hx:62
        b = s.b
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Output.hx:63
        k = _hx_len
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Output.hx:64
        while (k > 0):
            # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Output.hx:74
            self.writeByte(b[pos])
            # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Output.hx:76
            pos = (pos + 1)
            # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Output.hx:77
            k = (k - 1)
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Output.hx:79
        return _hx_len

    def flush(self):
        pass

    def close(self):
        pass

    def set_bigEndian(self,b):
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Output.hx:95
        self.bigEndian = b
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Output.hx:96
        return b

    def writeFullBytes(self,s,pos,_hx_len):
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Output.hx:121
        while (_hx_len > 0):
            # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Output.hx:122
            k = self.writeBytes(s,pos,_hx_len)
            # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Output.hx:123
            pos = (pos + k)
            # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Output.hx:124
            _hx_len = (_hx_len - k)

    def prepare(self,nbytes):
        pass

    def writeString(self,s,encoding = None):
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Output.hx:282
        b = haxe_io_Bytes.ofString(s,encoding)
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Output.hx:284
        self.writeFullBytes(b,0,b.length)

haxe_io_Output._hx_class = haxe_io_Output


class haxe_io_BytesOutput(haxe_io_Output):
    _hx_class_name = "haxe.io.BytesOutput"
    _hx_is_interface = "False"
    __slots__ = ("b",)
    _hx_fields = ["b"]
    _hx_methods = ["writeByte", "writeBytes", "getBytes"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_io_Output


    def __init__(self):
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/BytesOutput.hx:40
        self.b = haxe_io_BytesBuffer()
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/BytesOutput.hx:43
        self.set_bigEndian(False)

    def writeByte(self,c):
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/BytesOutput.hx:55
        self.b.b.append(c)

    def writeBytes(self,buf,pos,_hx_len):
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/BytesOutput.hx:65
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/BytesOutput.hx:65
        _this = self.b
        if (((pos < 0) or ((_hx_len < 0))) or (((pos + _hx_len) > buf.length))):
            raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
        _this.b.extend(buf.b[pos:(pos + _hx_len)])
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/BytesOutput.hx:67
        return _hx_len

    def getBytes(self):
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/BytesOutput.hx:143
        return self.b.getBytes()

haxe_io_BytesOutput._hx_class = haxe_io_BytesOutput

class haxe_io_Encoding(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.io.Encoding"
    _hx_constructs = ["UTF8", "RawNative"]
haxe_io_Encoding.UTF8 = haxe_io_Encoding("UTF8", 0, ())
haxe_io_Encoding.RawNative = haxe_io_Encoding("RawNative", 1, ())
haxe_io_Encoding._hx_class = haxe_io_Encoding


class haxe_io_Eof:
    _hx_class_name = "haxe.io.Eof"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_methods = ["toString"]

    def __init__(self):
        pass

    def toString(self):
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Eof.hx:33
        return "Eof"

haxe_io_Eof._hx_class = haxe_io_Eof

class haxe_io_Error(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.io.Error"
    _hx_constructs = ["Blocked", "Overflow", "OutsideBounds", "Custom"]

    @staticmethod
    def Custom(e):
        return haxe_io_Error("Custom", 3, (e,))
haxe_io_Error.Blocked = haxe_io_Error("Blocked", 0, ())
haxe_io_Error.Overflow = haxe_io_Error("Overflow", 1, ())
haxe_io_Error.OutsideBounds = haxe_io_Error("OutsideBounds", 2, ())
haxe_io_Error._hx_class = haxe_io_Error


class haxe_io_Input:
    _hx_class_name = "haxe.io.Input"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_methods = ["readByte", "readBytes"]

    def readByte(self):
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Input.hx:53
        raise haxe_exceptions_NotImplementedException(None,None,_hx_AnonObject({'fileName': "haxe/io/Input.hx", 'lineNumber': 53, 'className': "haxe.io.Input", 'methodName': "readByte"}))

    def readBytes(self,s,pos,_hx_len):
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Input.hx:65
        k = _hx_len
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Input.hx:66
        b = s.b
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Input.hx:67
        if (((pos < 0) or ((_hx_len < 0))) or (((pos + _hx_len) > s.length))):
            raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Input.hx:69
        try:
            while (k > 0):
                # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Input.hx:78
                b[pos] = self.readByte()
                # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Input.hx:80
                pos = (pos + 1)
                # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Input.hx:81
                k = (k - 1)
        except BaseException as _g:
            # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Input.hx:83
            None
            # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Input.hx:69
            if (not Std.isOfType(haxe_Exception.caught(_g).unwrap(),haxe_io_Eof)):
                raise _g
        # /Users/glen/bin/haxe-4.2.5/std/haxe/io/Input.hx:84
        return (_hx_len - k)

haxe_io_Input._hx_class = haxe_io_Input


class haxe_iterators_ArrayIterator:
    _hx_class_name = "haxe.iterators.ArrayIterator"
    _hx_is_interface = "False"
    __slots__ = ("array", "current")
    _hx_fields = ["array", "current"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,array):
        # /Users/glen/bin/haxe-4.2.5/std/haxe/iterators/ArrayIterator.hx:30
        self.current = 0
        # /Users/glen/bin/haxe-4.2.5/std/haxe/iterators/ArrayIterator.hx:37
        self.array = array

    def hasNext(self):
        # /Users/glen/bin/haxe-4.2.5/std/haxe/iterators/ArrayIterator.hx:45
        return (self.current < len(self.array))

    def next(self):
        # /Users/glen/bin/haxe-4.2.5/std/haxe/iterators/ArrayIterator.hx:53
        def _hx_local_3():
            # /Users/glen/bin/haxe-4.2.5/std/haxe/iterators/ArrayIterator.hx:53
            def _hx_local_2():
                # /Users/glen/bin/haxe-4.2.5/std/haxe/iterators/ArrayIterator.hx:53
                _hx_local_0 = self
                _hx_local_1 = _hx_local_0.current
                _hx_local_0.current = (_hx_local_1 + 1)
                return _hx_local_1
            return python_internal_ArrayImpl._get(self.array, _hx_local_2())
        return _hx_local_3()

haxe_iterators_ArrayIterator._hx_class = haxe_iterators_ArrayIterator


class haxe_iterators_ArrayKeyValueIterator:
    _hx_class_name = "haxe.iterators.ArrayKeyValueIterator"
    _hx_is_interface = "False"
    __slots__ = ("current", "array")
    _hx_fields = ["current", "array"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,array):
        # /Users/glen/bin/haxe-4.2.5/std/haxe/iterators/ArrayKeyValueIterator.hx:27
        self.current = 0
        # /Users/glen/bin/haxe-4.2.5/std/haxe/iterators/ArrayKeyValueIterator.hx:32
        self.array = array

    def hasNext(self):
        # /Users/glen/bin/haxe-4.2.5/std/haxe/iterators/ArrayKeyValueIterator.hx:37
        return (self.current < len(self.array))

    def next(self):
        # /Users/glen/bin/haxe-4.2.5/std/haxe/iterators/ArrayKeyValueIterator.hx:42
        def _hx_local_3():
            # /Users/glen/bin/haxe-4.2.5/std/haxe/iterators/ArrayKeyValueIterator.hx:42
            def _hx_local_2():
                # /Users/glen/bin/haxe-4.2.5/std/haxe/iterators/ArrayKeyValueIterator.hx:42
                _hx_local_0 = self
                _hx_local_1 = _hx_local_0.current
                _hx_local_0.current = (_hx_local_1 + 1)
                return _hx_local_1
            return _hx_AnonObject({'value': python_internal_ArrayImpl._get(self.array, self.current), 'key': _hx_local_2()})
        return _hx_local_3()

haxe_iterators_ArrayKeyValueIterator._hx_class = haxe_iterators_ArrayKeyValueIterator


class python_Boot:
    _hx_class_name = "python.Boot"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["keywords", "toString1", "fields", "simpleField", "hasField", "field", "getInstanceFields", "getSuperClass", "getClassFields", "prefixLength", "unhandleKeywords"]

    @staticmethod
    def toString1(o,s):
        # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:87
        if (o is None):
            return "null"
        # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:90
        if isinstance(o,str):
            return o
        # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:93
        if (s is None):
            s = ""
        # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:95
        if (len(s) >= 5):
            return "<...>"
        # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:98
        if isinstance(o,bool):
            if o:
                return "true"
            else:
                return "false"
        # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:104
        if (isinstance(o,int) and (not isinstance(o,bool))):
            return str(o)
        # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:108
        if isinstance(o,float):
            try:
                if (o == int(o)):
                    return str(Math.floor((o + 0.5)))
                else:
                    return str(o)
            except BaseException as _g:
                # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:115
                None
                # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:116
                return str(o)
        # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:120
        if isinstance(o,list):
            # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:121
            o1 = o
            # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:123
            l = len(o1)
            # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:125
            st = "["
            # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:126
            s = (("null" if s is None else s) + "\t")
            # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:127
            # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:127
            _g = 0
            _g1 = l
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:128
                prefix = ""
                # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:129
                if (i > 0):
                    prefix = ","
                # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:132
                st = (("null" if st is None else st) + HxOverrides.stringOrNull(((("null" if prefix is None else prefix) + HxOverrides.stringOrNull(python_Boot.toString1((o1[i] if i >= 0 and i < len(o1) else None),s))))))
            # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:134
            st = (("null" if st is None else st) + "]")
            # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:135
            return st
        # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:138
        try:
            if hasattr(o,"toString"):
                return o.toString()
        except BaseException as _g:
            None
        # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:143
        if hasattr(o,"__class__"):
            # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:144
            if isinstance(o,_hx_AnonObject):
                # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:145
                toStr = None
                # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:146
                try:
                    # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:147
                    fields = python_Boot.fields(o)
                    # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:148
                    _g = []
                    _g1 = 0
                    while (_g1 < len(fields)):
                        f = (fields[_g1] if _g1 >= 0 and _g1 < len(fields) else None)
                        _g1 = (_g1 + 1)
                        x = ((("" + ("null" if f is None else f)) + " : ") + HxOverrides.stringOrNull(python_Boot.toString1(python_Boot.simpleField(o,f),(("null" if s is None else s) + "\t"))))
                        _g.append(x)
                    fieldsStr = _g
                    # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:149
                    toStr = (("{ " + HxOverrides.stringOrNull(", ".join([x1 for x1 in fieldsStr]))) + " }")
                except BaseException as _g:
                    # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:150
                    None
                    # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:151
                    return "{ ... }"
                # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:154
                if (toStr is None):
                    return "{ ... }"
                else:
                    return toStr
            # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:160
            if isinstance(o,Enum):
                # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:161
                o1 = o
                # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:163
                l = len(o1.params)
                # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:164
                hasParams = (l > 0)
                # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:165
                if hasParams:
                    # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:166
                    paramsStr = ""
                    # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:167
                    # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:167
                    _g = 0
                    _g1 = l
                    while (_g < _g1):
                        i = _g
                        _g = (_g + 1)
                        # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:168
                        prefix = ""
                        # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:169
                        if (i > 0):
                            prefix = ","
                        # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:172
                        paramsStr = (("null" if paramsStr is None else paramsStr) + HxOverrides.stringOrNull(((("null" if prefix is None else prefix) + HxOverrides.stringOrNull(python_Boot.toString1(o1.params[i],s))))))
                    # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:174
                    return (((HxOverrides.stringOrNull(o1.tag) + "(") + ("null" if paramsStr is None else paramsStr)) + ")")
                else:
                    return o1.tag
            # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:180
            if hasattr(o,"_hx_class_name"):
                if (o.__class__.__name__ != "type"):
                    # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:182
                    fields = python_Boot.getInstanceFields(o)
                    # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:183
                    _g = []
                    _g1 = 0
                    while (_g1 < len(fields)):
                        f = (fields[_g1] if _g1 >= 0 and _g1 < len(fields) else None)
                        _g1 = (_g1 + 1)
                        x = ((("" + ("null" if f is None else f)) + " : ") + HxOverrides.stringOrNull(python_Boot.toString1(python_Boot.simpleField(o,f),(("null" if s is None else s) + "\t"))))
                        _g.append(x)
                    fieldsStr = _g
                    # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:185
                    toStr = (((HxOverrides.stringOrNull(o._hx_class_name) + "( ") + HxOverrides.stringOrNull(", ".join([x1 for x1 in fieldsStr]))) + " )")
                    # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:186
                    return toStr
                else:
                    # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:188
                    fields = python_Boot.getClassFields(o)
                    # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:189
                    _g = []
                    _g1 = 0
                    while (_g1 < len(fields)):
                        f = (fields[_g1] if _g1 >= 0 and _g1 < len(fields) else None)
                        _g1 = (_g1 + 1)
                        x = ((("" + ("null" if f is None else f)) + " : ") + HxOverrides.stringOrNull(python_Boot.toString1(python_Boot.simpleField(o,f),(("null" if s is None else s) + "\t"))))
                        _g.append(x)
                    fieldsStr = _g
                    # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:190
                    toStr = (((("#" + HxOverrides.stringOrNull(o._hx_class_name)) + "( ") + HxOverrides.stringOrNull(", ".join([x1 for x1 in fieldsStr]))) + " )")
                    # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:191
                    return toStr
            # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:195
            if ((type(o) == type) and (o == str)):
                return "#String"
            # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:199
            if ((type(o) == type) and (o == list)):
                return "#Array"
            # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:203
            if callable(o):
                return "function"
            # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:206
            try:
                if hasattr(o,"__repr__"):
                    return o.__repr__()
            except BaseException as _g:
                None
            # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:212
            if hasattr(o,"__str__"):
                return o.__str__([])
            # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:216
            if hasattr(o,"__name__"):
                return o.__name__
            # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:219
            return "???"
        else:
            return str(o)

    @staticmethod
    def fields(o):
        # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:231
        a = []
        # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:232
        if (o is not None):
            # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:233
            if hasattr(o,"_hx_fields"):
                # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:234
                fields = o._hx_fields
                # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:235
                if (fields is not None):
                    return list(fields)
            # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:239
            if isinstance(o,_hx_AnonObject):
                # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:240
                d = o.__dict__
                # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:241
                keys = d.keys()
                # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:242
                handler = python_Boot.unhandleKeywords
                # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:244
                for k in keys:
                # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:245
                    if (k != '_hx_disable_getattr'):
                # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:246
                        a.append(handler(k))
            elif hasattr(o,"__dict__"):
                # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:249
                d = o.__dict__
                # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:250
                keys1 = d.keys()
                # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:251
                for k in keys1:
                # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:252
                    a.append(k)
        # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:255
        return a

    @staticmethod
    def simpleField(o,field):
        # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:267
        if (field is None):
            return None
        # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:270
        field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
        # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:271
        if hasattr(o,field1):
            return getattr(o,field1)
        else:
            return None

    @staticmethod
    def hasField(o,field):
        # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:280
        if isinstance(o,_hx_AnonObject):
            return o._hx_hasattr(field)
        # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:283
        return hasattr(o,(("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field)))

    @staticmethod
    def field(o,field):
        # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:287
        if (field is None):
            return None
        # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:295
        if isinstance(o,str):
            # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:296
            field1 = field
            _hx_local_0 = len(field1)
            # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:306
            if (_hx_local_0 == 10):
                if (field1 == "charCodeAt"):
                    return python_internal_MethodClosure(o,HxString.charCodeAt)
                else:
                    # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:320
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_0 == 11):
                if (field1 == "lastIndexOf"):
                    return python_internal_MethodClosure(o,HxString.lastIndexOf)
                elif (field1 == "toLowerCase"):
                    return python_internal_MethodClosure(o,HxString.toLowerCase)
                elif (field1 == "toUpperCase"):
                    return python_internal_MethodClosure(o,HxString.toUpperCase)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_0 == 9):
                if (field1 == "substring"):
                    return python_internal_MethodClosure(o,HxString.substring)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_0 == 5):
                if (field1 == "split"):
                    return python_internal_MethodClosure(o,HxString.split)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_0 == 7):
                if (field1 == "indexOf"):
                    return python_internal_MethodClosure(o,HxString.indexOf)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_0 == 8):
                if (field1 == "toString"):
                    return python_internal_MethodClosure(o,HxString.toString)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_0 == 6):
                if (field1 == "charAt"):
                    return python_internal_MethodClosure(o,HxString.charAt)
                elif (field1 == "length"):
                    return len(o)
                elif (field1 == "substr"):
                    return python_internal_MethodClosure(o,HxString.substr)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            else:
                field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                if hasattr(o,field1):
                    return getattr(o,field1)
                else:
                    return None
        elif isinstance(o,list):
            # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:323
            field1 = field
            _hx_local_1 = len(field1)
            # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:353
            if (_hx_local_1 == 11):
                if (field1 == "lastIndexOf"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.lastIndexOf)
                else:
                    # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:369
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_1 == 4):
                if (field1 == "copy"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.copy)
                elif (field1 == "join"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.join)
                elif (field1 == "push"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.push)
                elif (field1 == "sort"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.sort)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_1 == 5):
                if (field1 == "shift"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.shift)
                elif (field1 == "slice"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.slice)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_1 == 7):
                if (field1 == "indexOf"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.indexOf)
                elif (field1 == "reverse"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.reverse)
                elif (field1 == "unshift"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.unshift)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_1 == 3):
                if (field1 == "map"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.map)
                elif (field1 == "pop"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.pop)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_1 == 8):
                if (field1 == "contains"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.contains)
                elif (field1 == "iterator"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.iterator)
                elif (field1 == "toString"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.toString)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_1 == 16):
                if (field1 == "keyValueIterator"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.keyValueIterator)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_1 == 6):
                if (field1 == "concat"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.concat)
                elif (field1 == "filter"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.filter)
                elif (field1 == "insert"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.insert)
                elif (field1 == "length"):
                    return len(o)
                elif (field1 == "remove"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.remove)
                elif (field1 == "splice"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.splice)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            else:
                field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                if hasattr(o,field1):
                    return getattr(o,field1)
                else:
                    return None
        else:
            # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:372
            field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
            if hasattr(o,field1):
                return getattr(o,field1)
            else:
                return None

    @staticmethod
    def getInstanceFields(c):
        # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:377
        f = (list(c._hx_fields) if (hasattr(c,"_hx_fields")) else [])
        # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:378
        if hasattr(c,"_hx_methods"):
            f = (f + c._hx_methods)
        # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:381
        sc = python_Boot.getSuperClass(c)
        # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:383
        if (sc is None):
            return f
        else:
            # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:386
            scArr = python_Boot.getInstanceFields(sc)
            # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:387
            scMap = set(scArr)
            # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:388
            # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:388
            _g = 0
            while (_g < len(f)):
                f1 = (f[_g] if _g >= 0 and _g < len(f) else None)
                _g = (_g + 1)
                # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:389
                if (not (f1 in scMap)):
                    scArr.append(f1)
            # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:394
            return scArr

    @staticmethod
    def getSuperClass(c):
        # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:399
        if (c is None):
            return None
        # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:402
        try:
            # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:403
            if hasattr(c,"_hx_super"):
                return c._hx_super
            # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:406
            return None
        except BaseException as _g:
            None
        # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:408
        return None

    @staticmethod
    def getClassFields(c):
        # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:412
        if hasattr(c,"_hx_statics"):
            # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:413
            x = c._hx_statics
            # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:414
            return list(x)
        else:
            return []

    @staticmethod
    def unhandleKeywords(name):
        # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:439
        if (HxString.substr(name,0,python_Boot.prefixLength) == "_hx_"):
            # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:440
            real = HxString.substr(name,python_Boot.prefixLength,None)
            # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:441
            if (real in python_Boot.keywords):
                return real
        # /Users/glen/bin/haxe-4.2.5/std/python/Boot.hx:444
        return name
python_Boot._hx_class = python_Boot


class python_internal_ArrayImpl:
    _hx_class_name = "python.internal.ArrayImpl"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["concat", "copy", "iterator", "keyValueIterator", "indexOf", "lastIndexOf", "join", "toString", "pop", "push", "unshift", "remove", "contains", "shift", "slice", "sort", "splice", "map", "filter", "insert", "reverse", "_get", "_set"]

    @staticmethod
    def concat(a1,a2):
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/ArrayImpl.hx:35
        return (a1 + a2)

    @staticmethod
    def copy(x):
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/ArrayImpl.hx:40
        return list(x)

    @staticmethod
    def iterator(x):
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/ArrayImpl.hx:45
        return python_HaxeIterator(x.__iter__())

    @staticmethod
    def keyValueIterator(x):
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/ArrayImpl.hx:50
        return haxe_iterators_ArrayKeyValueIterator(x)

    @staticmethod
    def indexOf(a,x,fromIndex = None):
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/ArrayImpl.hx:55
        _hx_len = len(a)
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/ArrayImpl.hx:56
        l = (0 if ((fromIndex is None)) else ((_hx_len + fromIndex) if ((fromIndex < 0)) else fromIndex))
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/ArrayImpl.hx:57
        if (l < 0):
            l = 0
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/ArrayImpl.hx:59
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/ArrayImpl.hx:59
        _g = l
        _g1 = _hx_len
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            # /Users/glen/bin/haxe-4.2.5/std/python/internal/ArrayImpl.hx:60
            if HxOverrides.eq(a[i],x):
                return i
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/ArrayImpl.hx:63
        return -1

    @staticmethod
    def lastIndexOf(a,x,fromIndex = None):
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/ArrayImpl.hx:68
        _hx_len = len(a)
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/ArrayImpl.hx:69
        l = (_hx_len if ((fromIndex is None)) else (((_hx_len + fromIndex) + 1) if ((fromIndex < 0)) else (fromIndex + 1)))
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/ArrayImpl.hx:70
        if (l > _hx_len):
            l = _hx_len
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/ArrayImpl.hx:72
        while True:
            # /Users/glen/bin/haxe-4.2.5/std/python/internal/ArrayImpl.hx:72
            l = (l - 1)
            tmp = l
            if (not ((tmp > -1))):
                break
            # /Users/glen/bin/haxe-4.2.5/std/python/internal/ArrayImpl.hx:73
            if HxOverrides.eq(a[l],x):
                return l
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/ArrayImpl.hx:76
        return -1

    @staticmethod
    def join(x,sep):
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/ArrayImpl.hx:82
        return sep.join([python_Boot.toString1(x1,'') for x1 in x])

    @staticmethod
    def toString(x):
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/ArrayImpl.hx:87
        return (("[" + HxOverrides.stringOrNull(",".join([python_Boot.toString1(x1,'') for x1 in x]))) + "]")

    @staticmethod
    def pop(x):
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/ArrayImpl.hx:92
        if (len(x) == 0):
            return None
        else:
            return x.pop()

    @staticmethod
    def push(x,e):
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/ArrayImpl.hx:97
        x.append(e)
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/ArrayImpl.hx:98
        return len(x)

    @staticmethod
    def unshift(x,e):
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/ArrayImpl.hx:103
        x.insert(0, e)

    @staticmethod
    def remove(x,e):
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/ArrayImpl.hx:108
        try:
            # /Users/glen/bin/haxe-4.2.5/std/python/internal/ArrayImpl.hx:109
            x.remove(e)
            # /Users/glen/bin/haxe-4.2.5/std/python/internal/ArrayImpl.hx:110
            return True
        except BaseException as _g:
            # /Users/glen/bin/haxe-4.2.5/std/python/internal/ArrayImpl.hx:111
            None
            # /Users/glen/bin/haxe-4.2.5/std/python/internal/ArrayImpl.hx:112
            return False

    @staticmethod
    def contains(x,e):
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/ArrayImpl.hx:118
        return (e in x)

    @staticmethod
    def shift(x):
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/ArrayImpl.hx:123
        if (len(x) == 0):
            return None
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/ArrayImpl.hx:125
        return x.pop(0)

    @staticmethod
    def slice(x,pos,end = None):
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/ArrayImpl.hx:130
        return x[pos:end]

    @staticmethod
    def sort(x,f):
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/ArrayImpl.hx:135
        x.sort(key= python_lib_Functools.cmp_to_key(f))

    @staticmethod
    def splice(x,pos,_hx_len):
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/ArrayImpl.hx:140
        if (pos < 0):
            pos = (len(x) + pos)
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/ArrayImpl.hx:142
        if (pos < 0):
            pos = 0
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/ArrayImpl.hx:144
        res = x[pos:(pos + _hx_len)]
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/ArrayImpl.hx:145
        del x[pos:(pos + _hx_len)]
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/ArrayImpl.hx:146
        return res

    @staticmethod
    def map(x,f):
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/ArrayImpl.hx:151
        return list(map(f,x))

    @staticmethod
    def filter(x,f):
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/ArrayImpl.hx:156
        return list(filter(f,x))

    @staticmethod
    def insert(a,pos,x):
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/ArrayImpl.hx:161
        a.insert(pos, x)

    @staticmethod
    def reverse(a):
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/ArrayImpl.hx:166
        a.reverse()

    @staticmethod
    def _get(x,idx):
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/ArrayImpl.hx:171
        if ((idx > -1) and ((idx < len(x)))):
            return x[idx]
        else:
            return None

    @staticmethod
    def _set(x,idx,v):
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/ArrayImpl.hx:176
        l = len(x)
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/ArrayImpl.hx:177
        while (l < idx):
            # /Users/glen/bin/haxe-4.2.5/std/python/internal/ArrayImpl.hx:178
            x.append(None)
            # /Users/glen/bin/haxe-4.2.5/std/python/internal/ArrayImpl.hx:179
            l = (l + 1)
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/ArrayImpl.hx:181
        if (l == idx):
            x.append(v)
        else:
            x[idx] = v
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/ArrayImpl.hx:186
        return v
python_internal_ArrayImpl._hx_class = python_internal_ArrayImpl


class HxOverrides:
    _hx_class_name = "HxOverrides"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["iterator", "eq", "stringOrNull", "mapKwArgs"]

    @staticmethod
    def iterator(x):
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/HxOverrides.hx:37
        if isinstance(x,list):
            return haxe_iterators_ArrayIterator(x)
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/HxOverrides.hx:40
        return x.iterator()

    @staticmethod
    def eq(a,b):
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/HxOverrides.hx:53
        if (isinstance(a,list) or isinstance(b,list)):
            return a is b
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/HxOverrides.hx:56
        return (a == b)

    @staticmethod
    def stringOrNull(s):
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/HxOverrides.hx:61
        if (s is None):
            return "null"
        else:
            return s

    @staticmethod
    def mapKwArgs(a,v):
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/HxOverrides.hx:204
        a1 = _hx_AnonObject(python_Lib.anonToDict(a))
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/HxOverrides.hx:205
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/HxOverrides.hx:205
        k = python_HaxeIterator(iter(v.keys()))
        while k.hasNext():
            k1 = k.next()
            # /Users/glen/bin/haxe-4.2.5/std/python/internal/HxOverrides.hx:206
            val = v.get(k1)
            # /Users/glen/bin/haxe-4.2.5/std/python/internal/HxOverrides.hx:207
            if a1._hx_hasattr(k1):
                # /Users/glen/bin/haxe-4.2.5/std/python/internal/HxOverrides.hx:208
                x = getattr(a1,k1)
                # /Users/glen/bin/haxe-4.2.5/std/python/internal/HxOverrides.hx:209
                setattr(a1,val,x)
                # /Users/glen/bin/haxe-4.2.5/std/python/internal/HxOverrides.hx:210
                delattr(a1,k1)
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/HxOverrides.hx:213
        return a1
HxOverrides._hx_class = HxOverrides


class python_internal_MethodClosure:
    _hx_class_name = "python.internal.MethodClosure"
    _hx_is_interface = "False"
    __slots__ = ("obj", "func")
    _hx_fields = ["obj", "func"]
    _hx_methods = ["__call__"]

    def __init__(self,obj,func):
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/MethodClosure.hx:30
        self.obj = obj
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/MethodClosure.hx:31
        self.func = func

    def __call__(self,*args):
        # /Users/glen/bin/haxe-4.2.5/std/python/internal/MethodClosure.hx:35
        return self.func(self.obj,*args)

python_internal_MethodClosure._hx_class = python_internal_MethodClosure


class sys_net_Socket:
    _hx_class_name = "sys.net.Socket"
    _hx_is_interface = "False"
    __slots__ = ("_hx___s", "input", "output")
    _hx_fields = ["__s", "input", "output"]
    _hx_methods = ["__initSocket", "close", "connect", "shutdown", "setTimeout", "fileno"]

    def __init__(self):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/net/Socket.hx:115
        self.output = None
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/net/Socket.hx:113
        self.input = None
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/net/Socket.hx:111
        self._hx___s = None
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/net/Socket.hx:120
        self._hx___initSocket()
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/net/Socket.hx:121
        self.input = sys_net__Socket_SocketInput(self._hx___s)
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/net/Socket.hx:122
        self.output = sys_net__Socket_SocketOutput(self._hx___s)

    def _hx___initSocket(self):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/net/Socket.hx:126
        self._hx___s = python_lib_socket_Socket()

    def close(self):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/net/Socket.hx:130
        self._hx___s.close()

    def connect(self,host,port):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/net/Socket.hx:142
        host_str = host.toString()
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/net/Socket.hx:143
        self._hx___s.connect((host_str, port))

    def shutdown(self,read,write):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/net/Socket.hx:151
        self._hx___s.shutdown((python_lib_Socket.SHUT_RDWR if ((read and write)) else (python_lib_Socket.SHUT_RD if read else python_lib_Socket.SHUT_WR)))

    def setTimeout(self,timeout):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/net/Socket.hx:178
        self._hx___s.settimeout(timeout)

    def fileno(self):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/net/Socket.hx:194
        return self._hx___s.fileno()

sys_net_Socket._hx_class = sys_net_Socket


class python_net_SslSocket(sys_net_Socket):
    _hx_class_name = "python.net.SslSocket"
    _hx_is_interface = "False"
    __slots__ = ("hostName",)
    _hx_fields = ["hostName"]
    _hx_methods = ["__initSocket", "connect"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = sys_net_Socket


    def __init__(self):
        # /Users/glen/bin/haxe-4.2.5/std/python/net/SslSocket.hx:31
        self.hostName = None
        # /Users/glen/bin/haxe-4.2.5/std/python/net/SslSocket.hx:30
        super().__init__()

    def _hx___initSocket(self):
        # /Users/glen/bin/haxe-4.2.5/std/python/net/SslSocket.hx:38
        context = python_lib_ssl_SSLContext(python_lib_Ssl.PROTOCOL_SSLv23)
        # /Users/glen/bin/haxe-4.2.5/std/python/net/SslSocket.hx:39
        context.verify_mode = python_lib_Ssl.CERT_REQUIRED
        # /Users/glen/bin/haxe-4.2.5/std/python/net/SslSocket.hx:40
        context.set_default_verify_paths()
        # /Users/glen/bin/haxe-4.2.5/std/python/net/SslSocket.hx:41
        context.options = (context.options | python_lib_Ssl.OP_NO_SSLv2)
        # /Users/glen/bin/haxe-4.2.5/std/python/net/SslSocket.hx:42
        context.options = (context.options | python_lib_Ssl.OP_NO_SSLv3)
        # /Users/glen/bin/haxe-4.2.5/std/python/net/SslSocket.hx:43
        context.options = (context.options | python_lib_Ssl.OP_NO_COMPRESSION)
        # /Users/glen/bin/haxe-4.2.5/std/python/net/SslSocket.hx:45
        context.options = (context.options | python_lib_Ssl.OP_NO_TLSv1)
        # /Users/glen/bin/haxe-4.2.5/std/python/net/SslSocket.hx:46
        self._hx___s = python_lib_socket_Socket()
        # /Users/glen/bin/haxe-4.2.5/std/python/net/SslSocket.hx:47
        self._hx___s = context.wrap_socket(self._hx___s,False,True,True,self.hostName)

    def connect(self,host,port):
        # /Users/glen/bin/haxe-4.2.5/std/python/net/SslSocket.hx:51
        self.hostName = host.host
        # /Users/glen/bin/haxe-4.2.5/std/python/net/SslSocket.hx:52
        super().connect(host,port)

python_net_SslSocket._hx_class = python_net_SslSocket


class sys_Http(haxe_http_HttpBase):
    _hx_class_name = "sys.Http"
    _hx_is_interface = "False"
    __slots__ = ("noShutdown", "cnxTimeout", "responseHeaders", "chunk_size", "chunk_buf", "file")
    _hx_fields = ["noShutdown", "cnxTimeout", "responseHeaders", "chunk_size", "chunk_buf", "file"]
    _hx_methods = ["request", "customRequest", "writeBody", "readHttpResponse", "readChunk"]
    _hx_statics = ["PROXY", "requestUrl"]
    _hx_interfaces = []
    _hx_super = haxe_http_HttpBase


    def __init__(self,url):
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:38
        self.file = None
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:37
        self.chunk_buf = None
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:36
        self.chunk_size = None
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:34
        self.responseHeaders = None
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:32
        self.noShutdown = None
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:49
        self.cnxTimeout = 10
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:53
        super().__init__(url)

    def request(self,post = None):
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:56
        _gthis = self
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:57
        output = haxe_io_BytesOutput()
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:58
        old = self.onError
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:59
        err = False
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:60
        def _hx_local_0(e):
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:60
            nonlocal err
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:61
            _gthis.responseBytes = output.getBytes()
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:62
            err = True
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:64
            _gthis.onError = old
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:65
            _gthis.onError(e)
        self.onError = _hx_local_0
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:67
        post = ((post or ((self.postBytes is not None))) or ((self.postData is not None)))
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:68
        self.customRequest(post,output)
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:69
        if (not err):
            self.success(output.getBytes())

    def customRequest(self,post,api,sock = None,method = None):
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:91
        self.responseAsString = None
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:92
        self.responseBytes = None
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:93
        url_regexp = EReg("^(https?://)?([a-zA-Z\\.0-9_-]+)(:[0-9]+)?(.*)$","")
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:94
        url_regexp.matchObj = python_lib_Re.search(url_regexp.pattern,self.url)
        if (url_regexp.matchObj is None):
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:95
            self.onError("Invalid URL")
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:96
            return
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:98
        secure = (url_regexp.matchObj.group(1) == "https://")
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:99
        if (sock is None):
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:100
            if secure:
                sock = python_net_SslSocket()
            else:
                sock = sys_net_Socket()
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:117
            sock.setTimeout(self.cnxTimeout)
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:119
        host = url_regexp.matchObj.group(2)
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:120
        portString = url_regexp.matchObj.group(3)
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:121
        request = url_regexp.matchObj.group(4)
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:125
        if ((("" if ((0 >= len(request))) else request[0])) != "/"):
            request = ("/" + ("null" if request is None else request))
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:128
        port = ((443 if secure else 80) if (((portString is None) or ((portString == "")))) else Std.parseInt(HxString.substr(portString,1,(len(portString) - 1))))
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:130
        multipart = (self.file is not None)
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:131
        boundary = None
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:132
        uri = None
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:133
        if multipart:
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:134
            post = True
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:135
            boundary = (((Std.string(int((python_lib_Random.random() * 1000))) + Std.string(int((python_lib_Random.random() * 1000)))) + Std.string(int((python_lib_Random.random() * 1000)))) + Std.string(int((python_lib_Random.random() * 1000))))
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:139
            while (len(boundary) < 38):
                boundary = ("-" + ("null" if boundary is None else boundary))
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:141
            b_b = python_lib_io_StringIO()
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:142
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:142
            _g = 0
            _g1 = self.params
            while (_g < len(_g1)):
                p = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
                _g = (_g + 1)
                # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:143
                b_b.write("--")
                # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:144
                b_b.write(Std.string(boundary))
                # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:145
                b_b.write("\r\n")
                # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:146
                b_b.write("Content-Disposition: form-data; name=\"")
                # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:147
                b_b.write(Std.string(p.name))
                # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:148
                b_b.write("\"")
                # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:149
                b_b.write("\r\n")
                # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:150
                b_b.write("\r\n")
                # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:151
                b_b.write(Std.string(p.value))
                # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:152
                b_b.write("\r\n")
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:154
            b_b.write("--")
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:155
            b_b.write(Std.string(boundary))
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:156
            b_b.write("\r\n")
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:157
            b_b.write("Content-Disposition: form-data; name=\"")
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:158
            b_b.write(Std.string(self.file.param))
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:159
            b_b.write("\"; filename=\"")
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:160
            b_b.write(Std.string(self.file.filename))
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:161
            b_b.write("\"")
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:162
            b_b.write("\r\n")
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:163
            b_b.write(Std.string(((("Content-Type: " + HxOverrides.stringOrNull(self.file.mimeType)) + "\r\n") + "\r\n")))
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:164
            uri = b_b.getvalue()
        else:
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:166
            _g = 0
            _g1 = self.params
            while (_g < len(_g1)):
                p = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
                _g = (_g + 1)
                # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:167
                if (uri is None):
                    uri = ""
                else:
                    uri = (("null" if uri is None else uri) + "&")
                # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:171
                uri = (("null" if uri is None else uri) + HxOverrides.stringOrNull((((HxOverrides.stringOrNull(python_lib_urllib_Parse.quote(p.name,"")) + "=") + HxOverrides.stringOrNull(python_lib_urllib_Parse.quote(("" + HxOverrides.stringOrNull(p.value)),""))))))
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:175
        b = haxe_io_BytesOutput()
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:176
        if (method is not None):
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:177
            b.writeString(method)
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:178
            b.writeString(" ")
        elif post:
            b.writeString("POST ")
        else:
            b.writeString("GET ")
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:184
        if (sys_Http.PROXY is not None):
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:185
            b.writeString("http://")
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:186
            b.writeString(host)
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:187
            if (port != 80):
                # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:188
                b.writeString(":")
                # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:189
                b.writeString(("" + Std.string(port)))
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:192
        b.writeString(request)
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:194
        if ((not post) and ((uri is not None))):
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:195
            if (HxString.indexOfImpl(request,"?",0) >= 0):
                b.writeString("&")
            else:
                b.writeString("?")
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:199
            b.writeString(uri)
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:201
        b.writeString(((" HTTP/1.1\r\nHost: " + ("null" if host is None else host)) + "\r\n"))
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:202
        if (self.postData is not None):
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:203
            self.postBytes = haxe_io_Bytes.ofString(self.postData)
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:204
            self.postData = None
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:206
        if (self.postBytes is not None):
            b.writeString((("Content-Length: " + Std.string(self.postBytes.length)) + "\r\n"))
        elif (post and ((uri is not None))):
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:209
            def _hx_local_4(h):
                # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:209
                return (h.name == "Content-Type")
            if (multipart or (not Lambda.exists(self.headers,_hx_local_4))):
                # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:210
                b.writeString("Content-Type: ")
                # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:211
                if multipart:
                    # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:212
                    b.writeString("multipart/form-data")
                    # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:213
                    b.writeString("; boundary=")
                    # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:214
                    b.writeString(boundary)
                else:
                    b.writeString("application/x-www-form-urlencoded")
                # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:217
                b.writeString("\r\n")
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:219
            if multipart:
                b.writeString((("Content-Length: " + Std.string(((((len(uri) + self.file.size) + len(boundary)) + 6)))) + "\r\n"))
            else:
                b.writeString((("Content-Length: " + Std.string(len(uri))) + "\r\n"))
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:224
        b.writeString("Connection: close\r\n")
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:225
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:225
        _g = 0
        _g1 = self.headers
        while (_g < len(_g1)):
            h = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:226
            b.writeString(h.name)
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:227
            b.writeString(": ")
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:228
            b.writeString(h.value)
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:229
            b.writeString("\r\n")
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:231
        b.writeString("\r\n")
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:232
        if (self.postBytes is not None):
            b.writeFullBytes(self.postBytes,0,self.postBytes.length)
        elif (post and ((uri is not None))):
            b.writeString(uri)
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:236
        try:
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:237
            if (sys_Http.PROXY is not None):
                sock.connect(sys_net_Host(sys_Http.PROXY.host),sys_Http.PROXY.port)
            else:
                sock.connect(sys_net_Host(host),port)
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:241
            if multipart:
                self.writeBody(b,self.file.io,self.file.size,boundary,sock)
            else:
                self.writeBody(b,None,0,None,sock)
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:245
            self.readHttpResponse(api,sock)
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:246
            sock.close()
        except BaseException as _g:
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:247
            None
            e = haxe_Exception.caught(_g).unwrap()
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:248
            try:
                sock.close()
            except BaseException as _g:
                pass
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:251
            self.onError(Std.string(e))

    def writeBody(self,body,fileInput,fileSize,boundary,sock):
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:256
        if (body is not None):
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:257
            _hx_bytes = body.getBytes()
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:258
            sock.output.writeFullBytes(_hx_bytes,0,_hx_bytes.length)
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:260
        if (boundary is not None):
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:261
            bufsize = 4096
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:262
            buf = haxe_io_Bytes.alloc(bufsize)
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:263
            while (fileSize > 0):
                # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:264
                size = (bufsize if ((fileSize > bufsize)) else fileSize)
                # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:265
                _hx_len = 0
                # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:266
                try:
                    _hx_len = fileInput.readBytes(buf,0,size)
                except BaseException as _g:
                    # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:268
                    None
                    # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:266
                    if Std.isOfType(haxe_Exception.caught(_g).unwrap(),haxe_io_Eof):
                        break
                    else:
                        raise _g
                # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:270
                sock.output.writeFullBytes(buf,0,_hx_len)
                # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:271
                fileSize = (fileSize - _hx_len)
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:273
            sock.output.writeString("\r\n")
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:274
            sock.output.writeString("--")
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:275
            sock.output.writeString(boundary)
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:276
            sock.output.writeString("--")

    def readHttpResponse(self,api,sock):
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:282
        b = haxe_io_BytesBuffer()
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:283
        k = 4
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:284
        s = haxe_io_Bytes.alloc(4)
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:285
        sock.setTimeout(self.cnxTimeout)
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:286
        while True:
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:287
            p = sock.input.readBytes(s,0,k)
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:288
            while (p != k):
                p = (p + sock.input.readBytes(s,p,(k - p)))
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:290
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:290
            if ((k < 0) or ((k > s.length))):
                raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
            b.b.extend(s.b[0:k])
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:291
            k1 = k
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:292
            if (k1 == 1):
                # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:293
                c = s.b[0]
                # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:294
                if (c == 10):
                    break
                # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:296
                if (c == 13):
                    k = 3
                else:
                    k = 4
            elif (k1 == 2):
                # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:301
                c1 = s.b[1]
                # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:302
                if (c1 == 10):
                    # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:303
                    if (s.b[0] == 13):
                        break
                    # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:305
                    k = 4
                elif (c1 == 13):
                    k = 3
                else:
                    k = 4
            elif (k1 == 3):
                # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:311
                c2 = s.b[2]
                # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:312
                if (c2 == 10):
                    if (s.b[1] != 13):
                        k = 4
                    elif (s.b[0] != 10):
                        k = 2
                    else:
                        break
                elif (c2 == 13):
                    if ((s.b[1] != 10) or ((s.b[0] != 13))):
                        k = 1
                    else:
                        k = 3
                else:
                    k = 4
            elif (k1 == 4):
                # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:327
                c3 = s.b[3]
                # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:328
                if (c3 == 10):
                    if (s.b[2] != 13):
                        continue
                    elif ((s.b[1] != 10) or ((s.b[0] != 13))):
                        k = 2
                    else:
                        break
                elif (c3 == 13):
                    if ((s.b[2] != 10) or ((s.b[1] != 13))):
                        k = 3
                    else:
                        k = 1
            else:
                pass
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:346
        _this = b.getBytes().toString()
        headers = _this.split("\r\n")
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:348
        response = (None if ((len(headers) == 0)) else headers.pop(0))
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:349
        rp = response.split(" ")
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:350
        status = Std.parseInt((rp[1] if 1 < len(rp) else None))
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:351
        if ((status == 0) or ((status is None))):
            raise haxe_Exception.thrown("Response status error")
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:355
        if (len(headers) != 0):
            headers.pop()
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:356
        if (len(headers) != 0):
            headers.pop()
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:357
        self.responseHeaders = haxe_ds_StringMap()
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:358
        size = None
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:359
        chunked = False
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:360
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:360
        _g = 0
        while (_g < len(headers)):
            hline = (headers[_g] if _g >= 0 and _g < len(headers) else None)
            _g = (_g + 1)
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:361
            a = hline.split(": ")
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:362
            hname = (None if ((len(a) == 0)) else a.pop(0))
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:363
            hval = ((a[0] if 0 < len(a) else None) if ((len(a) == 1)) else ": ".join([python_Boot.toString1(x1,'') for x1 in a]))
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:364
            hval = StringTools.ltrim(StringTools.rtrim(hval))
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:365
            self.responseHeaders.h[hname] = hval
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:366
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:366
            _g1 = hname.lower()
            _hx_local_2 = len(_g1)
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:370
            if (_hx_local_2 == 17):
                if (_g1 == "transfer-encoding"):
                    chunked = (hval.lower() == "chunked")
            elif (_hx_local_2 == 14):
                if (_g1 == "content-length"):
                    size = Std.parseInt(hval)
            else:
                pass
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:374
        self.onStatus(status)
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:376
        chunk_re = EReg("^([0-9A-Fa-f]+)[ ]*\r\n","m")
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:377
        self.chunk_size = None
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:378
        self.chunk_buf = None
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:380
        bufsize = 1024
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:381
        buf = haxe_io_Bytes.alloc(bufsize)
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:382
        if chunked:
            try:
                while True:
                    # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:385
                    _hx_len = sock.input.readBytes(buf,0,bufsize)
                    # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:386
                    if (not self.readChunk(chunk_re,api,buf,_hx_len)):
                        break
            except BaseException as _g:
                # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:389
                None
                # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:383
                if Std.isOfType(haxe_Exception.caught(_g).unwrap(),haxe_io_Eof):
                    raise haxe_Exception.thrown("Transfer aborted")
                else:
                    raise _g
        elif (size is None):
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:393
            if (not self.noShutdown):
                sock.shutdown(False,True)
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:395
            try:
                while True:
                    # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:397
                    _hx_len = sock.input.readBytes(buf,0,bufsize)
                    # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:398
                    if (_hx_len == 0):
                        break
                    # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:400
                    api.writeBytes(buf,0,_hx_len)
            except BaseException as _g:
                # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:402
                None
                # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:395
                if (not Std.isOfType(haxe_Exception.caught(_g).unwrap(),haxe_io_Eof)):
                    raise _g
        else:
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:404
            api.prepare(size)
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:405
            try:
                while (size > 0):
                    # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:407
                    _hx_len = sock.input.readBytes(buf,0,(bufsize if ((size > bufsize)) else size))
                    # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:408
                    api.writeBytes(buf,0,_hx_len)
                    # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:409
                    size = (size - _hx_len)
            except BaseException as _g:
                # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:411
                None
                # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:405
                if Std.isOfType(haxe_Exception.caught(_g).unwrap(),haxe_io_Eof):
                    raise haxe_Exception.thrown("Transfer aborted")
                else:
                    raise _g
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:415
        if (chunked and (((self.chunk_size is not None) or ((self.chunk_buf is not None))))):
            raise haxe_Exception.thrown("Invalid chunk")
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:417
        if ((status < 200) or ((status >= 400))):
            raise haxe_Exception.thrown(("Http Error #" + Std.string(status)))
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:419
        api.close()

    def readChunk(self,chunk_re,api,buf,_hx_len):
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:423
        if (self.chunk_size is None):
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:424
            if (self.chunk_buf is not None):
                # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:425
                b = haxe_io_BytesBuffer()
                # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:426
                b.b.extend(self.chunk_buf.b)
                # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:427
                # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:427
                if ((_hx_len < 0) or ((_hx_len > buf.length))):
                    raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
                b.b.extend(buf.b[0:_hx_len])
                # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:428
                buf = b.getBytes()
                # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:429
                _hx_len = (_hx_len + self.chunk_buf.length)
                # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:430
                self.chunk_buf = None
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:435
            s = buf.toString()
            chunk_re.matchObj = python_lib_Re.search(chunk_re.pattern,s)
            if (chunk_re.matchObj is not None):
                # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:437
                p_pos = chunk_re.matchObj.start()
                p_len = (chunk_re.matchObj.end() - chunk_re.matchObj.start())
                # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:438
                if (p_len <= _hx_len):
                    # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:439
                    cstr = chunk_re.matchObj.group(1)
                    # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:440
                    self.chunk_size = Std.parseInt(("0x" + ("null" if cstr is None else cstr)))
                    # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:441
                    if (self.chunk_size == 0):
                        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:442
                        self.chunk_size = None
                        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:443
                        self.chunk_buf = None
                        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:444
                        return False
                    # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:446
                    _hx_len = (_hx_len - p_len)
                    # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:447
                    return self.readChunk(chunk_re,api,buf.sub(p_len,_hx_len),_hx_len)
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:451
            if (_hx_len > 10):
                # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:452
                self.onError("Invalid chunk")
                # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:453
                return False
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:455
            self.chunk_buf = buf.sub(0,_hx_len)
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:456
            return True
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:459
        if (self.chunk_size > _hx_len):
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:460
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:460
            _hx_local_2 = self
            _hx_local_3 = _hx_local_2.chunk_size
            _hx_local_2.chunk_size = (_hx_local_3 - _hx_len)
            _hx_local_2.chunk_size
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:461
            api.writeBytes(buf,0,_hx_len)
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:462
            return True
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:464
        end = (self.chunk_size + 2)
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:465
        if (_hx_len >= end):
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:466
            if (self.chunk_size > 0):
                api.writeBytes(buf,0,self.chunk_size)
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:468
            _hx_len = (_hx_len - end)
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:469
            self.chunk_size = None
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:470
            if (_hx_len == 0):
                return True
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:472
            return self.readChunk(chunk_re,api,buf.sub(end,_hx_len),_hx_len)
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:474
        if (self.chunk_size > 0):
            api.writeBytes(buf,0,self.chunk_size)
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:476
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:476
        _hx_local_5 = self
        _hx_local_6 = _hx_local_5.chunk_size
        _hx_local_5.chunk_size = (_hx_local_6 - _hx_len)
        _hx_local_5.chunk_size
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:477
        return True

    @staticmethod
    def requestUrl(url):
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:489
        h = sys_Http(url)
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:490
        r = None
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:492
        def _hx_local_0(d):
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:492
            nonlocal r
            r = d
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:491
        h.onData = _hx_local_0
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:495
        def _hx_local_1(e):
            # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:495
            raise haxe_Exception.thrown(e)
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:494
        h.onError = _hx_local_1
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:497
        h.request(False)
        # /Users/glen/bin/haxe-4.2.5/std/sys/Http.hx:498
        return r

sys_Http._hx_class = sys_Http


class sys_net_Host:
    _hx_class_name = "sys.net.Host"
    _hx_is_interface = "False"
    __slots__ = ("host", "name")
    _hx_fields = ["host", "name"]
    _hx_methods = ["toString"]

    def __init__(self,name):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/net/Host.hx:32
        self.host = name
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/net/Host.hx:33
        self.name = name

    def toString(self):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/net/Host.hx:37
        return self.name

sys_net_Host._hx_class = sys_net_Host


class sys_net__Socket_SocketInput(haxe_io_Input):
    _hx_class_name = "sys.net._Socket.SocketInput"
    _hx_is_interface = "False"
    __slots__ = ("_hx___s",)
    _hx_fields = ["__s"]
    _hx_methods = ["readByte", "readBytes"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_io_Input


    def __init__(self,s):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/net/Socket.hx:39
        self._hx___s = s

    def readByte(self):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/net/Socket.hx:43
        r = None
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/net/Socket.hx:44
        try:
            r = self._hx___s.recv(1,0)
        except BaseException as _g:
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/net/Socket.hx:46
            None
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/net/Socket.hx:44
            if Std.isOfType(haxe_Exception.caught(_g).unwrap(),BlockingIOError):
                raise haxe_Exception.thrown(haxe_io_Error.Blocked)
            else:
                raise _g
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/net/Socket.hx:49
        if (len(r) == 0):
            raise haxe_Exception.thrown(haxe_io_Eof())
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/net/Socket.hx:51
        return r[0]

    def readBytes(self,buf,pos,_hx_len):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/net/Socket.hx:55
        r = None
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/net/Socket.hx:56
        data = buf.b
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/net/Socket.hx:57
        try:
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/net/Socket.hx:58
            r = self._hx___s.recv(_hx_len,0)
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/net/Socket.hx:59
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/net/Socket.hx:59
            _g = pos
            _g1 = (pos + len(r))
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/net/Socket.hx:60
                data.__setitem__(i,r[(i - pos)])
        except BaseException as _g:
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/net/Socket.hx:62
            None
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/net/Socket.hx:57
            if Std.isOfType(haxe_Exception.caught(_g).unwrap(),BlockingIOError):
                raise haxe_Exception.thrown(haxe_io_Error.Blocked)
            else:
                raise _g
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/net/Socket.hx:65
        if (len(r) == 0):
            raise haxe_Exception.thrown(haxe_io_Eof())
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/net/Socket.hx:67
        return len(r)

sys_net__Socket_SocketInput._hx_class = sys_net__Socket_SocketInput


class sys_net__Socket_SocketOutput(haxe_io_Output):
    _hx_class_name = "sys.net._Socket.SocketOutput"
    _hx_is_interface = "False"
    __slots__ = ("_hx___s",)
    _hx_fields = ["__s"]
    _hx_methods = ["writeByte", "writeBytes", "close"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_io_Output


    def __init__(self,s):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/net/Socket.hx:81
        self._hx___s = s

    def writeByte(self,c):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/net/Socket.hx:85
        try:
            self._hx___s.send(bytes([c]),0)
        except BaseException as _g:
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/net/Socket.hx:87
            None
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/net/Socket.hx:85
            if Std.isOfType(haxe_Exception.caught(_g).unwrap(),BlockingIOError):
                raise haxe_Exception.thrown(haxe_io_Error.Blocked)
            else:
                raise _g

    def writeBytes(self,buf,pos,_hx_len):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/net/Socket.hx:93
        try:
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/net/Socket.hx:94
            data = buf.b
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/net/Socket.hx:95
            payload = data[pos:pos+_hx_len]
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/net/Socket.hx:96
            r = self._hx___s.send(payload,0)
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/net/Socket.hx:97
            return r
        except BaseException as _g:
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/net/Socket.hx:98
            None
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/net/Socket.hx:93
            if Std.isOfType(haxe_Exception.caught(_g).unwrap(),BlockingIOError):
                raise haxe_Exception.thrown(haxe_io_Error.Blocked)
            else:
                raise _g

    def close(self):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/net/Socket.hx:104
        super().close()
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/net/Socket.hx:105
        if (self._hx___s is not None):
            self._hx___s.close()

sys_net__Socket_SocketOutput._hx_class = sys_net__Socket_SocketOutput


class sys_thread_EventLoop:
    _hx_class_name = "sys.thread.EventLoop"
    _hx_is_interface = "False"
    __slots__ = ("mutex", "oneTimeEvents", "oneTimeEventsIdx", "waitLock", "promisedEventsCount", "regularEvents")
    _hx_fields = ["mutex", "oneTimeEvents", "oneTimeEventsIdx", "waitLock", "promisedEventsCount", "regularEvents"]
    _hx_methods = ["repeat", "cancel", "loop"]

    def __init__(self):
        # /Users/glen/bin/haxe-4.2.5/std/sys/thread/EventLoop.hx:30
        self.regularEvents = None
        # /Users/glen/bin/haxe-4.2.5/std/sys/thread/EventLoop.hx:29
        self.promisedEventsCount = 0
        # /Users/glen/bin/haxe-4.2.5/std/sys/thread/EventLoop.hx:28
        self.waitLock = sys_thread_Lock()
        # /Users/glen/bin/haxe-4.2.5/std/sys/thread/EventLoop.hx:27
        self.oneTimeEventsIdx = 0
        # /Users/glen/bin/haxe-4.2.5/std/sys/thread/EventLoop.hx:26
        self.oneTimeEvents = list()
        # /Users/glen/bin/haxe-4.2.5/std/sys/thread/EventLoop.hx:25
        self.mutex = sys_thread_Mutex()

    def repeat(self,event,intervalMs):
        # /Users/glen/bin/haxe-4.2.5/std/sys/thread/EventLoop.hx:38
        self.mutex.lock.acquire(True)
        # /Users/glen/bin/haxe-4.2.5/std/sys/thread/EventLoop.hx:39
        interval = (0.001 * intervalMs)
        # /Users/glen/bin/haxe-4.2.5/std/sys/thread/EventLoop.hx:40
        event1 = sys_thread__EventLoop_RegularEvent(event,(python_lib_Time.time() + interval),interval)
        # /Users/glen/bin/haxe-4.2.5/std/sys/thread/EventLoop.hx:41
        # /Users/glen/bin/haxe-4.2.5/std/sys/thread/EventLoop.hx:41
        _g = self.regularEvents
        if (_g is None):
            self.regularEvents = event1
        else:
            current = _g
            previous = None
            while True:
                if (current is None):
                    previous.next = event1
                    event1.previous = previous
                    break
                elif (event1.nextRunTime < current.nextRunTime):
                    event1.next = current
                    current.previous = event1
                    if (previous is None):
                        self.regularEvents = event1
                    else:
                        event1.previous = previous
                        previous.next = event1
                        current.previous = event1
                    break
                else:
                    previous = current
                    current = current.next
        # /Users/glen/bin/haxe-4.2.5/std/sys/thread/EventLoop.hx:42
        self.waitLock.semaphore.release()
        # /Users/glen/bin/haxe-4.2.5/std/sys/thread/EventLoop.hx:43
        self.mutex.lock.release()
        # /Users/glen/bin/haxe-4.2.5/std/sys/thread/EventLoop.hx:44
        return event1

    def cancel(self,eventHandler):
        # /Users/glen/bin/haxe-4.2.5/std/sys/thread/EventLoop.hx:82
        self.mutex.lock.acquire(True)
        # /Users/glen/bin/haxe-4.2.5/std/sys/thread/EventLoop.hx:83
        event = eventHandler
        # /Users/glen/bin/haxe-4.2.5/std/sys/thread/EventLoop.hx:84
        event.cancelled = True
        # /Users/glen/bin/haxe-4.2.5/std/sys/thread/EventLoop.hx:85
        if (self.regularEvents == event):
            self.regularEvents = event.next
        # /Users/glen/bin/haxe-4.2.5/std/sys/thread/EventLoop.hx:88
        # /Users/glen/bin/haxe-4.2.5/std/sys/thread/EventLoop.hx:88
        _g = event.next
        # /Users/glen/bin/haxe-4.2.5/std/sys/thread/EventLoop.hx:89
        if (_g is not None):
            # /Users/glen/bin/haxe-4.2.5/std/sys/thread/EventLoop.hx:90
            e = _g
            e.previous = event.previous
        # /Users/glen/bin/haxe-4.2.5/std/sys/thread/EventLoop.hx:92
        # /Users/glen/bin/haxe-4.2.5/std/sys/thread/EventLoop.hx:92
        _g = event.previous
        # /Users/glen/bin/haxe-4.2.5/std/sys/thread/EventLoop.hx:93
        if (_g is not None):
            # /Users/glen/bin/haxe-4.2.5/std/sys/thread/EventLoop.hx:94
            e = _g
            e.next = event.next
        # /Users/glen/bin/haxe-4.2.5/std/sys/thread/EventLoop.hx:96
        self.mutex.lock.release()

    def loop(self):
        # /Users/glen/bin/haxe-4.2.5/std/sys/thread/EventLoop.hx:174
        recycleRegular = []
        # /Users/glen/bin/haxe-4.2.5/std/sys/thread/EventLoop.hx:175
        recycleOneTimers = []
        # /Users/glen/bin/haxe-4.2.5/std/sys/thread/EventLoop.hx:176
        while True:
            # /Users/glen/bin/haxe-4.2.5/std/sys/thread/EventLoop.hx:177
            now = python_lib_Time.time()
            regularsToRun = recycleRegular
            eventsToRunIdx = 0
            nextEventAt = -1
            self.mutex.lock.acquire(True)
            while self.waitLock.semaphore.acquire(True,0.0):
                pass
            current = self.regularEvents
            while (current is not None):
                if (current.nextRunTime <= now):
                    tmp = eventsToRunIdx
                    eventsToRunIdx = (eventsToRunIdx + 1)
                    python_internal_ArrayImpl._set(regularsToRun, tmp, current)
                    current.nextRunTime = (current.nextRunTime + current.interval)
                    # /Users/glen/bin/haxe-4.2.5/std/sys/thread/EventLoop.hx:214
                    nextEventAt = -2
                elif ((nextEventAt == -1) or ((current.nextRunTime < nextEventAt))):
                    nextEventAt = current.nextRunTime
                # /Users/glen/bin/haxe-4.2.5/std/sys/thread/EventLoop.hx:218
                current = current.next
            self.mutex.lock.release()
            _g = 0
            _g1 = eventsToRunIdx
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                if (not (regularsToRun[i] if i >= 0 and i < len(regularsToRun) else None).cancelled):
                    (regularsToRun[i] if i >= 0 and i < len(regularsToRun) else None).run()
                python_internal_ArrayImpl._set(regularsToRun, i, None)
            # /Users/glen/bin/haxe-4.2.5/std/sys/thread/EventLoop.hx:228
            eventsToRunIdx = 0
            # /Users/glen/bin/haxe-4.2.5/std/sys/thread/EventLoop.hx:177
            oneTimersToRun = recycleOneTimers
            self.mutex.lock.acquire(True)
            _g2_current = 0
            _g2_array = self.oneTimeEvents
            while (_g2_current < len(_g2_array)):
                _g3_value = (_g2_array[_g2_current] if _g2_current >= 0 and _g2_current < len(_g2_array) else None)
                _g3_key = _g2_current
                _g2_current = (_g2_current + 1)
                i1 = _g3_key
                event = _g3_value
                if (event is None):
                    break
                else:
                    tmp1 = eventsToRunIdx
                    eventsToRunIdx = (eventsToRunIdx + 1)
                    python_internal_ArrayImpl._set(oneTimersToRun, tmp1, event)
                    python_internal_ArrayImpl._set(self.oneTimeEvents, i1, None)
            self.oneTimeEventsIdx = 0
            hasPromisedEvents = (self.promisedEventsCount > 0)
            self.mutex.lock.release()
            _g2 = 0
            _g3 = eventsToRunIdx
            while (_g2 < _g3):
                i2 = _g2
                _g2 = (_g2 + 1)
                (oneTimersToRun[i2] if i2 >= 0 and i2 < len(oneTimersToRun) else None)()
                python_internal_ArrayImpl._set(oneTimersToRun, i2, None)
            if (eventsToRunIdx > 0):
                nextEventAt = -2
            r_nextEventAt = nextEventAt
            r_anyTime = hasPromisedEvents
            # /Users/glen/bin/haxe-4.2.5/std/sys/thread/EventLoop.hx:178
            # /Users/glen/bin/haxe-4.2.5/std/sys/thread/EventLoop.hx:178
            _g4 = r_anyTime
            _g5 = r_nextEventAt
            _g6 = _g5
            # /Users/glen/bin/haxe-4.2.5/std/sys/thread/EventLoop.hx:179
            if (_g6 == -2):
                pass
            elif (_g6 == -1):
                if _g4:
                    self.waitLock.semaphore.acquire(True,None)
                else:
                    break
            else:
                # /Users/glen/bin/haxe-4.2.5/std/sys/thread/EventLoop.hx:184
                time = _g5
                # /Users/glen/bin/haxe-4.2.5/std/sys/thread/EventLoop.hx:185
                timeout = (time - python_lib_Time.time())
                # /Users/glen/bin/haxe-4.2.5/std/sys/thread/EventLoop.hx:186
                # /Users/glen/bin/haxe-4.2.5/std/sys/thread/EventLoop.hx:186
                _this = self.waitLock
                timeout1 = (0 if (python_lib_Math.isnan(0)) else (timeout if (python_lib_Math.isnan(timeout)) else max(0,timeout)))
                _this.semaphore.acquire(True,timeout1)

sys_thread_EventLoop._hx_class = sys_thread_EventLoop


class sys_thread__EventLoop_RegularEvent:
    _hx_class_name = "sys.thread._EventLoop.RegularEvent"
    _hx_is_interface = "False"
    __slots__ = ("nextRunTime", "interval", "run", "next", "previous", "cancelled")
    _hx_fields = ["nextRunTime", "interval", "run", "next", "previous", "cancelled"]

    def __init__(self,run,nextRunTime,interval):
        # /Users/glen/bin/haxe-4.2.5/std/sys/thread/EventLoop.hx:267
        self.previous = None
        # /Users/glen/bin/haxe-4.2.5/std/sys/thread/EventLoop.hx:266
        self.next = None
        # /Users/glen/bin/haxe-4.2.5/std/sys/thread/EventLoop.hx:268
        self.cancelled = False
        # /Users/glen/bin/haxe-4.2.5/std/sys/thread/EventLoop.hx:271
        self.run = run
        # /Users/glen/bin/haxe-4.2.5/std/sys/thread/EventLoop.hx:272
        self.nextRunTime = nextRunTime
        # /Users/glen/bin/haxe-4.2.5/std/sys/thread/EventLoop.hx:273
        self.interval = interval

sys_thread__EventLoop_RegularEvent._hx_class = sys_thread__EventLoop_RegularEvent


class sys_thread_Lock:
    _hx_class_name = "sys.thread.Lock"
    _hx_is_interface = "False"
    __slots__ = ("semaphore",)
    _hx_fields = ["semaphore"]

    def __init__(self):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/thread/Lock.hx:30
        self.semaphore = Lock(0)

sys_thread_Lock._hx_class = sys_thread_Lock


class sys_thread_Mutex:
    _hx_class_name = "sys.thread.Mutex"
    _hx_is_interface = "False"
    __slots__ = ("lock",)
    _hx_fields = ["lock"]

    def __init__(self):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/thread/Mutex.hx:30
        self.lock = sys_thread__Mutex_NativeRLock()

sys_thread_Mutex._hx_class = sys_thread_Mutex


class sys_thread_NoEventLoopException(haxe_Exception):
    _hx_class_name = "sys.thread.NoEventLoopException"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_Exception


    def __init__(self,msg = None,previous = None):
        # /Users/glen/bin/haxe-4.2.5/std/sys/thread/NoEventLoopException.hx:6
        if (msg is None):
            msg = "Event loop is not available. Refer to sys.thread.Thread.runWithEventLoop."
        # /Users/glen/bin/haxe-4.2.5/std/sys/thread/NoEventLoopException.hx:7
        super().__init__(msg,previous)
sys_thread_NoEventLoopException._hx_class = sys_thread_NoEventLoopException


class sys_thread__Thread_Thread_Impl_:
    _hx_class_name = "sys.thread._Thread.Thread_Impl_"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["get_events", "processEvents"]
    events = None

    @staticmethod
    def get_events(this1):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/thread/Thread.hx:57
        if (this1.events is None):
            raise sys_thread_NoEventLoopException()
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/thread/Thread.hx:59
        return this1.events

    @staticmethod
    def processEvents():
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/thread/Thread.hx:64
        sys_thread__Thread_HxThread.current().events.loop()
sys_thread__Thread_Thread_Impl_._hx_class = sys_thread__Thread_Thread_Impl_


class sys_thread__Thread_HxThread:
    _hx_class_name = "sys.thread._Thread.HxThread"
    _hx_is_interface = "False"
    __slots__ = ("events", "nativeThread")
    _hx_fields = ["events", "nativeThread"]
    _hx_statics = ["threads", "threadsMutex", "mainThread", "current"]

    def __init__(self,t):
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/thread/Thread.hx:69
        self.events = None
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/thread/Thread.hx:86
        self.nativeThread = t
    threads = None
    threadsMutex = None
    mainThread = None

    @staticmethod
    def current():
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/thread/Thread.hx:94
        sys_thread__Thread_HxThread.threadsMutex.lock.acquire(True)
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/thread/Thread.hx:95
        ct = threading.current_thread()
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/thread/Thread.hx:96
        if (ct == threading.main_thread()):
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/thread/Thread.hx:97
            sys_thread__Thread_HxThread.threadsMutex.lock.release()
            # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/thread/Thread.hx:98
            return sys_thread__Thread_HxThread.mainThread
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/thread/Thread.hx:101
        if (not (ct in sys_thread__Thread_HxThread.threads.h)):
            sys_thread__Thread_HxThread.threads.set(ct,sys_thread__Thread_HxThread(ct))
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/thread/Thread.hx:104
        t = sys_thread__Thread_HxThread.threads.h.get(ct,None)
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/thread/Thread.hx:105
        sys_thread__Thread_HxThread.threadsMutex.lock.release()
        # /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/thread/Thread.hx:106
        return t

sys_thread__Thread_HxThread._hx_class = sys_thread__Thread_HxThread


class tink_core_Annex:
    _hx_class_name = "tink.core.Annex"
    _hx_is_interface = "False"
    __slots__ = ("target", "registry")
    _hx_fields = ["target", "registry"]

    def __init__(self,target):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Annex.hx:12
        self.target = target
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Annex.hx:13
        self.registry = haxe_ds_ObjectMap()

tink_core_Annex._hx_class = tink_core_Annex


class tink_core__Callback_Callback_Impl_:
    _hx_class_name = "tink.core._Callback.Callback_Impl_"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["_new", "toFunction", "depth", "MAX_DEPTH", "invoke", "fromNiladic", "fromMany", "defer"]

    @staticmethod
    def _new(f):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:7
        this1 = f
        return this1

    @staticmethod
    def toFunction(this1):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:11
        return this1

    @staticmethod
    def invoke(this1,data):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:25
        if (tink_core__Callback_Callback_Impl_.depth < 100):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:25
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:25
            _hx_local_0 = tink_core__Callback_Callback_Impl_
            _hx_local_1 = _hx_local_0.depth
            _hx_local_0.depth = (_hx_local_1 + 1)
            _hx_local_1
            this1(data)
            _hx_local_2 = tink_core__Callback_Callback_Impl_
            _hx_local_3 = _hx_local_2.depth
            _hx_local_2.depth = (_hx_local_3 - 1)
            _hx_local_3
        else:
            def _hx_local_4():
                this1(data)
            tink_core__Callback_Callback_Impl_.defer(_hx_local_4)

    @staticmethod
    def fromNiladic(f):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:28
        def _hx_local_0(_):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:28
            f()
        return _hx_local_0

    @staticmethod
    def fromMany(callbacks):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:32
        def _hx_local_0(v):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:33
            _g = 0
            while (_g < len(callbacks)):
                callback = (callbacks[_g] if _g >= 0 and _g < len(callbacks) else None)
                _g = (_g + 1)
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:34
                tink_core__Callback_Callback_Impl_.invoke(callback,v)
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:31
        return _hx_local_0

    @staticmethod
    def defer(f):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:50
        haxe_Timer.delay(f,0)
tink_core__Callback_Callback_Impl_._hx_class = tink_core__Callback_Callback_Impl_


class tink_core_LinkObject:
    _hx_class_name = "tink.core.LinkObject"
    _hx_is_interface = "True"
    __slots__ = ()
    _hx_methods = ["cancel"]
tink_core_LinkObject._hx_class = tink_core_LinkObject


class tink_core_CallbackLinkRef:
    _hx_class_name = "tink.core.CallbackLinkRef"
    _hx_is_interface = "False"
    __slots__ = ("link",)
    _hx_fields = ["link"]
    _hx_methods = ["cancel"]
    _hx_interfaces = [tink_core_LinkObject]

    def __init__(self):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:60
        self.link = None

    def cancel(self):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:63
        this1 = self.link
        if (this1 is not None):
            this1.cancel()

tink_core_CallbackLinkRef._hx_class = tink_core_CallbackLinkRef


class tink_core__Callback_CallbackLink_Impl_:
    _hx_class_name = "tink.core._Callback.CallbackLink_Impl_"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["_new", "cancel", "dissolve", "noop", "toFunction", "toCallback", "fromFunction", "join", "fromMany"]

    @staticmethod
    def _new(link):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:69
        this1 = tink_core_SimpleLink(link)
        return this1

    @staticmethod
    def cancel(this1):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:73
        if (this1 is not None):
            this1.cancel()

    @staticmethod
    def dissolve(this1):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:77
        if (this1 is not None):
            this1.cancel()

    @staticmethod
    def noop():
        pass

    @staticmethod
    def toFunction(this1):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:82
        if (this1 is None):
            return tink_core__Callback_CallbackLink_Impl_.noop
        else:
            return this1.cancel

    @staticmethod
    def toCallback(this1):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:85
        if (this1 is None):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:85
            def _hx_local_1():
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:85
                def _hx_local_0(_):
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:85
                    tink_core__Callback_CallbackLink_Impl_.noop()
                return _hx_local_0
            return _hx_local_1()
        else:
            f = this1.cancel
            def _hx_local_2(_):
                f()
            return _hx_local_2

    @staticmethod
    def fromFunction(f):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:88
        this1 = tink_core_SimpleLink(f)
        return this1

    @staticmethod
    def join(this1,b):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:91
        return tink_core__Callback_LinkPair(this1,b)

    @staticmethod
    def fromMany(callbacks):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:95
        def _hx_local_1():
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:95
            nonlocal callbacks
            if (callbacks is not None):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:96
                _g = 0
                while (_g < len(callbacks)):
                    cb = (callbacks[_g] if _g >= 0 and _g < len(callbacks) else None)
                    _g = (_g + 1)
                    if (cb is not None):
                        cb.cancel()
            else:
                callbacks = None
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:94
        this1 = tink_core_SimpleLink(_hx_local_1)
        return this1
tink_core__Callback_CallbackLink_Impl_._hx_class = tink_core__Callback_CallbackLink_Impl_


class tink_core_SimpleLink:
    _hx_class_name = "tink.core.SimpleLink"
    _hx_is_interface = "False"
    __slots__ = ("f",)
    _hx_fields = ["f"]
    _hx_methods = ["cancel"]
    _hx_interfaces = [tink_core_LinkObject]

    def __init__(self,f):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:106
        self.f = f

    def cancel(self):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:109
        if (self.f is not None):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:110
            self.f()
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:111
            self.f = None

tink_core_SimpleLink._hx_class = tink_core_SimpleLink


class tink_core__Callback_LinkPair:
    _hx_class_name = "tink.core._Callback.LinkPair"
    _hx_is_interface = "False"
    __slots__ = ("a", "b", "dissolved")
    _hx_fields = ["a", "b", "dissolved"]
    _hx_methods = ["cancel"]
    _hx_interfaces = [tink_core_LinkObject]

    def __init__(self,a,b):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:119
        self.dissolved = False
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:121
        self.a = a
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:122
        self.b = b

    def cancel(self):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:126
        if (not self.dissolved):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:127
            self.dissolved = True
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:128
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:128
            this1 = self.a
            if (this1 is not None):
                this1.cancel()
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:129
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:129
            this1 = self.b
            if (this1 is not None):
                this1.cancel()
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:130
            self.a = None
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:131
            self.b = None

tink_core__Callback_LinkPair._hx_class = tink_core__Callback_LinkPair


class tink_core__Callback_ListCell:
    _hx_class_name = "tink.core._Callback.ListCell"
    _hx_is_interface = "False"
    __slots__ = ("cb", "list")
    _hx_fields = ["cb", "list"]
    _hx_methods = ["invoke", "clear", "cancel"]
    _hx_interfaces = [tink_core_LinkObject]

    def __init__(self,cb,_hx_list):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:140
        if (cb is None):
            raise haxe_Exception.thrown("callback expected but null received")
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:141
        self.cb = cb
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:142
        self.list = _hx_list

    def invoke(self,data):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:146
        if (self.list is not None):
            self.cb(data)

    def clear(self):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:150
        self.cb = None
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:151
        self.list = None

    def cancel(self):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:155
        if (self.list is not None):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:156
            _hx_list = self.list
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:157
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:157
            self.cb = None
            self.list = None
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:158
            def _hx_local_1():
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:158
                _hx_list.used = (_hx_list.used - 1)
                return _hx_list.used
            tmp = _hx_local_1()
            if (tmp <= ((len(_hx_list.cells) >> 1))):
                _hx_list.compact()

tink_core__Callback_ListCell._hx_class = tink_core__Callback_ListCell


class tink_core_Disposable:
    _hx_class_name = "tink.core.Disposable"
    _hx_is_interface = "True"
    __slots__ = ()
    _hx_methods = ["get_disposed", "ondispose"]
tink_core_Disposable._hx_class = tink_core_Disposable


class tink_core_OwnedDisposable:
    _hx_class_name = "tink.core.OwnedDisposable"
    _hx_is_interface = "True"
    __slots__ = ()
    _hx_methods = ["dispose"]
    _hx_interfaces = [tink_core_Disposable]
tink_core_OwnedDisposable._hx_class = tink_core_OwnedDisposable


class tink_core_SimpleDisposable:
    _hx_class_name = "tink.core.SimpleDisposable"
    _hx_is_interface = "False"
    __slots__ = ("f", "disposeHandlers")
    _hx_fields = ["f", "disposeHandlers"]
    _hx_methods = ["get_disposed", "ondispose", "dispose"]
    _hx_statics = ["noop"]
    _hx_interfaces = [tink_core_OwnedDisposable]

    def __init__(self,dispose):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Disposable.hx:47
        self.disposeHandlers = []
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Disposable.hx:60
        self.f = dispose

    def get_disposed(self):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Disposable.hx:51
        return (self.disposeHandlers is None)

    def ondispose(self,d):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Disposable.hx:54
        _g = self.disposeHandlers
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Disposable.hx:55
        if (_g is None):
            d()
        else:
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Disposable.hx:56
            v = _g
            v.append(d)

    def dispose(self):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Disposable.hx:63
        _g = self.disposeHandlers
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Disposable.hx:64
        if (_g is not None):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Disposable.hx:65
            v = _g
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Disposable.hx:66
            self.disposeHandlers = None
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Disposable.hx:67
            f = self.f
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Disposable.hx:68
            self.f = tink_core_SimpleDisposable.noop
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Disposable.hx:69
            f()
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Disposable.hx:70
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Disposable.hx:70
            _g = 0
            while (_g < len(v)):
                h = (v[_g] if _g >= 0 and _g < len(v) else None)
                _g = (_g + 1)
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Disposable.hx:71
                h()

    @staticmethod
    def noop():
        pass

tink_core_SimpleDisposable._hx_class = tink_core_SimpleDisposable


class tink_core_CallbackList(tink_core_SimpleDisposable):
    _hx_class_name = "tink.core.CallbackList"
    _hx_is_interface = "False"
    __slots__ = ("destructive", "cells", "used", "queue", "busy", "ondrain", "onfill")
    _hx_fields = ["destructive", "cells", "used", "queue", "busy", "ondrain", "onfill"]
    _hx_methods = ["get_length", "release", "destroy", "drain", "add", "invoke", "compact", "resize", "clear"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = tink_core_SimpleDisposable


    def __init__(self,destructive = None):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:162
        if (destructive is None):
            destructive = False
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:165
        self.cells = None
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:164
        self.destructive = None
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:183
        def _hx_local_0():
            pass
        self.onfill = _hx_local_0
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:182
        def _hx_local_1():
            pass
        self.ondrain = _hx_local_1
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:174
        self.busy = False
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:172
        self.queue = []
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:171
        self.used = 0
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:176
        _gthis = self
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:177
        def _hx_local_2():
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:177
            if (not _gthis.busy):
                _gthis.destroy()
        super().__init__(_hx_local_2)
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:178
        self.destructive = destructive
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:179
        self.cells = []

    def get_length(self):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:169
        return self.used

    def release(self):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:186
        self.used = (self.used - 1)
        tmp = self.used
        if (tmp <= ((len(self.cells) >> 1))):
            self.compact()

    def destroy(self):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:190
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:190
        _g = 0
        _g1 = self.cells
        while (_g < len(_g1)):
            c = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:191
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:191
            c.cb = None
            c.list = None
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:193
        self.queue = None
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:194
        self.cells = None
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:196
        if (self.used > 0):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:197
            self.used = 0
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:198
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:198
            fn = self.ondrain
            if (tink_core__Callback_Callback_Impl_.depth < 100):
                _hx_local_1 = tink_core__Callback_Callback_Impl_
                _hx_local_2 = _hx_local_1.depth
                _hx_local_1.depth = (_hx_local_2 + 1)
                _hx_local_2
                fn()
                _hx_local_3 = tink_core__Callback_Callback_Impl_
                _hx_local_4 = _hx_local_3.depth
                _hx_local_3.depth = (_hx_local_4 - 1)
                _hx_local_4
            else:
                tink_core__Callback_Callback_Impl_.defer(fn)

    def drain(self):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:203
        fn = self.ondrain
        if (tink_core__Callback_Callback_Impl_.depth < 100):
            _hx_local_0 = tink_core__Callback_Callback_Impl_
            _hx_local_1 = _hx_local_0.depth
            _hx_local_0.depth = (_hx_local_1 + 1)
            _hx_local_1
            fn()
            _hx_local_2 = tink_core__Callback_Callback_Impl_
            _hx_local_3 = _hx_local_2.depth
            _hx_local_2.depth = (_hx_local_3 - 1)
            _hx_local_3
        else:
            tink_core__Callback_Callback_Impl_.defer(fn)

    def add(self,cb):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:206
        if (self.disposeHandlers is None):
            return None
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:207
        node = tink_core__Callback_ListCell(cb,self)
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:208
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:208
        _this = self.cells
        _this.append(node)
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:209
        def _hx_local_2():
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:209
            _hx_local_0 = self
            _hx_local_1 = _hx_local_0.used
            _hx_local_0.used = (_hx_local_1 + 1)
            return _hx_local_1
        tmp = (_hx_local_2() == 0)
        if tmp:
            fn = self.onfill
            if (tink_core__Callback_Callback_Impl_.depth < 100):
                _hx_local_3 = tink_core__Callback_Callback_Impl_
                _hx_local_4 = _hx_local_3.depth
                _hx_local_3.depth = (_hx_local_4 + 1)
                _hx_local_4
                fn()
                _hx_local_5 = tink_core__Callback_Callback_Impl_
                _hx_local_6 = _hx_local_5.depth
                _hx_local_5.depth = (_hx_local_6 - 1)
                _hx_local_6
            else:
                tink_core__Callback_Callback_Impl_.defer(fn)
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:210
        return node

    def invoke(self,data):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:214
        _gthis = self
        if (tink_core__Callback_Callback_Impl_.depth < 100):
            _hx_local_0 = tink_core__Callback_Callback_Impl_
            _hx_local_1 = _hx_local_0.depth
            _hx_local_0.depth = (_hx_local_1 + 1)
            _hx_local_1
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:215
            if (_gthis.disposeHandlers is not None):
                if _gthis.busy:
                    if (_gthis.destructive != True):
                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:218
                        _this = _gthis.queue
                        tmp = _this.append
                        _g = _gthis.invoke
                        data1 = data
                        def _hx_local_2():
                            _g(data1)
                        tmp(_hx_local_2)
                else:
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:221
                    _gthis.busy = True
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:223
                    if _gthis.destructive:
                        _gthis.dispose()
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:226
                    length = len(_gthis.cells)
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:227
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:227
                    _g1 = 0
                    _g2 = length
                    while (_g1 < _g2):
                        i = _g1
                        _g1 = (_g1 + 1)
                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:228
                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:228
                        _this = (_gthis.cells[i] if i >= 0 and i < len(_gthis.cells) else None)
                        if (_this.list is not None):
                            _this.cb(data)
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:230
                    _gthis.busy = False
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:232
                    if (_gthis.disposeHandlers is None):
                        _gthis.destroy()
                    else:
                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:235
                        if (_gthis.used < len(_gthis.cells)):
                            _gthis.compact()
                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:238
                        if (len(_gthis.queue) > 0):
                            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:239
                            _this = _gthis.queue
                            ((None if ((len(_this) == 0)) else _this.pop(0)))()
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:214
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:214
            _hx_local_3 = tink_core__Callback_Callback_Impl_
            _hx_local_4 = _hx_local_3.depth
            _hx_local_3.depth = (_hx_local_4 - 1)
            _hx_local_4
        else:
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:215
            def _hx_local_6():
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:215
                if (_gthis.disposeHandlers is not None):
                    if _gthis.busy:
                        if (_gthis.destructive != True):
                            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:218
                            _this = _gthis.queue
                            tmp = _this.append
                            _g = _gthis.invoke
                            data1 = data
                            def _hx_local_5():
                                _g(data1)
                            tmp(_hx_local_5)
                    else:
                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:221
                        _gthis.busy = True
                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:223
                        if _gthis.destructive:
                            _gthis.dispose()
                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:226
                        length = len(_gthis.cells)
                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:227
                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:227
                        _g1 = 0
                        _g2 = length
                        while (_g1 < _g2):
                            i = _g1
                            _g1 = (_g1 + 1)
                            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:228
                            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:228
                            _this = (_gthis.cells[i] if i >= 0 and i < len(_gthis.cells) else None)
                            if (_this.list is not None):
                                _this.cb(data)
                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:230
                        _gthis.busy = False
                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:232
                        if (_gthis.disposeHandlers is None):
                            _gthis.destroy()
                        else:
                            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:235
                            if (_gthis.used < len(_gthis.cells)):
                                _gthis.compact()
                            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:238
                            if (len(_gthis.queue) > 0):
                                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:239
                                _this = _gthis.queue
                                ((None if ((len(_this) == 0)) else _this.pop(0)))()
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:214
            tink_core__Callback_Callback_Impl_.defer(_hx_local_6)

    def compact(self):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:245
        if self.busy:
            return
        elif (self.used == 0):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:247
            self.resize(0)
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:248
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:248
            fn = self.ondrain
            if (tink_core__Callback_Callback_Impl_.depth < 100):
                _hx_local_0 = tink_core__Callback_Callback_Impl_
                _hx_local_1 = _hx_local_0.depth
                _hx_local_0.depth = (_hx_local_1 + 1)
                _hx_local_1
                fn()
                _hx_local_2 = tink_core__Callback_Callback_Impl_
                _hx_local_3 = _hx_local_2.depth
                _hx_local_2.depth = (_hx_local_3 - 1)
                _hx_local_3
            else:
                tink_core__Callback_Callback_Impl_.defer(fn)
        else:
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:251
            compacted = 0
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:253
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:253
            _g = 0
            _g1 = len(self.cells)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:254
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:254
                _g2 = (self.cells[i] if i >= 0 and i < len(self.cells) else None)
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:255
                _g3 = _g2.list
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:255
                if (_g2.cb is not None):
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:256
                    v = _g2
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:257
                    if (compacted != i):
                        python_internal_ArrayImpl._set(self.cells, compacted, v)
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:259
                    compacted = (compacted + 1)
                    tmp = compacted
                    if (tmp == self.used):
                        break
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:262
            self.resize(self.used)

    def resize(self,length):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:266
        _this = self.cells
        l = len(_this)
        if (l < length):
            idx = (length - 1)
            v = None
            l1 = len(_this)
            while (l1 < idx):
                _this.append(None)
                l1 = (l1 + 1)
            if (l1 == idx):
                _this.append(v)
            else:
                _this[idx] = v
        elif (l > length):
            pos = length
            _hx_len = (l - length)
            if (pos < 0):
                pos = (len(_this) + pos)
            if (pos < 0):
                pos = 0
            res = _this[pos:(pos + _hx_len)]
            del _this[pos:(pos + _hx_len)]

    def clear(self):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:270
        if self.busy:
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:271
            _this = self.queue
            _this.append(self.clear)
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:272
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:272
        _g = 0
        _g1 = self.cells
        while (_g < len(_g1)):
            cell = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:273
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:273
            cell.cb = None
            cell.list = None
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Callback.hx:274
        self.resize(0)

tink_core_CallbackList._hx_class = tink_core_CallbackList


class tink_core_AlreadyDisposed:
    _hx_class_name = "tink.core.AlreadyDisposed"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_methods = ["get_disposed", "ondispose", "dispose"]
    _hx_statics = ["INST"]
    _hx_interfaces = [tink_core_OwnedDisposable]

    def __init__(self):
        pass

    def get_disposed(self):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Disposable.hx:80
        return True

    def ondispose(self,d):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Disposable.hx:82
        d()

    def dispose(self):
        pass

tink_core_AlreadyDisposed._hx_class = tink_core_AlreadyDisposed


class tink_core_TypedError:
    _hx_class_name = "tink.core.TypedError"
    _hx_is_interface = "False"
    __slots__ = ("message", "code", "data", "pos", "callStack", "exceptionStack", "isTinkError")
    _hx_fields = ["message", "code", "data", "pos", "callStack", "exceptionStack", "isTinkError"]
    _hx_methods = ["printPos", "toString", "toPromise", "throwSelf"]
    _hx_statics = ["withData", "typed", "asError", "catchExceptions", "reporter", "rethrow", "tryFinally"]

    def __init__(self,code = None,message = None,pos = None):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Error.hx:49
        if (code is None):
            code = 500
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Error.hx:52
        self.data = None
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Error.hx:56
        self.isTinkError = True
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Error.hx:59
        self.code = code
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Error.hx:60
        self.message = message
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Error.hx:61
        self.pos = pos
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Error.hx:62
        self.exceptionStack = []
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Error.hx:63
        self.callStack = []

    def printPos(self):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Error.hx:66
        return ((((HxOverrides.stringOrNull(self.pos.className) + ".") + HxOverrides.stringOrNull(self.pos.methodName)) + ":") + Std.string(self.pos.lineNumber))

    def toString(self):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Error.hx:76
        ret = ((("Error#" + Std.string(self.code)) + ": ") + HxOverrides.stringOrNull(self.message))
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Error.hx:78
        if (self.pos is not None):
            ret = (("null" if ret is None else ret) + HxOverrides.stringOrNull(((" @ " + HxOverrides.stringOrNull(self.printPos())))))
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Error.hx:81
        return ret

    def toPromise(self):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Error.hx:85
        return tink_core__Future_SyncFuture(tink_core__Lazy_LazyConst(tink_core_Outcome.Failure(self)))

    def throwSelf(self):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Error.hx:96
        any = self
        raise haxe_Exception.thrown(any)

    @staticmethod
    def withData(code = None,message = None,data = None,pos = None):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Error.hx:100
        return tink_core_TypedError.typed(code,message,data,pos)

    @staticmethod
    def typed(code = None,message = None,data = None,pos = None):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Error.hx:104
        ret = tink_core_TypedError(code,message,pos)
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Error.hx:105
        ret.data = data
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Error.hx:106
        return ret

    @staticmethod
    def asError(v):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Error.hx:120
        return Std.downcast(v,tink_core_TypedError)

    @staticmethod
    def catchExceptions(f,report = None,pos = None):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Error.hx:130
        try:
            return tink_core_Outcome.Success(f())
        except BaseException as _g:
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Error.hx:132
            None
            e = haxe_Exception.caught(_g).unwrap()
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Error.hx:133
            e1 = tink_core_TypedError.asError(e)
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Error.hx:135
            tmp = None
            if (e1 is None):
                tmp = (tink_core_TypedError.withData(None,"Unexpected Error",e1,pos) if ((report is None)) else report(e1))
            else:
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Error.hx:141
                e = e1
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Error.hx:135
                tmp = e
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Error.hx:134
            return tink_core_Outcome.Failure(tmp)

    @staticmethod
    def reporter(code = None,message = None,pos = None):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Error.hx:148
        def _hx_local_0(e):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Error.hx:148
            return tink_core_TypedError.withData(code,message,e,pos)
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Error.hx:147
        return _hx_local_0

    @staticmethod
    def rethrow(any):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Error.hx:158
        raise haxe_Exception.thrown(any)

    @staticmethod
    def tryFinally(f,cleanup):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Error.hx:172
        try:
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Error.hx:173
            ret = f()
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Error.hx:174
            cleanup()
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Error.hx:175
            return ret
        except BaseException as _g:
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Error.hx:177
            None
            e = haxe_Exception.caught(_g).unwrap()
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Error.hx:178
            cleanup()
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Error.hx:179
            raise haxe_Exception.thrown(e)

tink_core_TypedError._hx_class = tink_core_TypedError


class tink_core__Error_Stack_Impl_:
    _hx_class_name = "tink.core._Error.Stack_Impl_"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["toString"]

    @staticmethod
    def toString(this1):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Error.hx:189
        return "Error stack not available. Compile with -D error_stack."
tink_core__Error_Stack_Impl_._hx_class = tink_core__Error_Stack_Impl_


class tink_core__Future_FutureObject:
    _hx_class_name = "tink.core._Future.FutureObject"
    _hx_is_interface = "True"
    __slots__ = ()
    _hx_methods = ["getStatus", "handle", "eager"]
tink_core__Future_FutureObject._hx_class = tink_core__Future_FutureObject


class tink_core__Future_NeverFuture:
    _hx_class_name = "tink.core._Future.NeverFuture"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_methods = ["getStatus", "handle", "eager"]
    _hx_interfaces = [tink_core__Future_FutureObject]

    def __init__(self):
        pass

    def getStatus(self):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:372
        return tink_core_FutureStatus.NeverEver

    def handle(self,callback):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:373
        return None

    def eager(self):
        pass

tink_core__Future_NeverFuture._hx_class = tink_core__Future_NeverFuture


class tink_core__Lazy_Computable:
    _hx_class_name = "tink.core._Lazy.Computable"
    _hx_is_interface = "True"
    __slots__ = ()
    _hx_methods = ["isComputed", "compute", "underlying"]
tink_core__Lazy_Computable._hx_class = tink_core__Lazy_Computable


class tink_core__Lazy_LazyObject:
    _hx_class_name = "tink.core._Lazy.LazyObject"
    _hx_is_interface = "True"
    __slots__ = ()
    _hx_methods = ["get"]
    _hx_interfaces = [tink_core__Lazy_Computable]
tink_core__Lazy_LazyObject._hx_class = tink_core__Lazy_LazyObject


class tink_core__Lazy_LazyConst:
    _hx_class_name = "tink.core._Lazy.LazyConst"
    _hx_is_interface = "False"
    __slots__ = ("value",)
    _hx_fields = ["value"]
    _hx_methods = ["isComputed", "get", "compute", "underlying"]
    _hx_interfaces = [tink_core__Lazy_LazyObject]

    def __init__(self,value):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Lazy.hx:52
        self.value = value

    def isComputed(self):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Lazy.hx:49
        return True

    def get(self):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Lazy.hx:55
        return self.value

    def compute(self):
        pass

    def underlying(self):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Lazy.hx:60
        return None

tink_core__Lazy_LazyConst._hx_class = tink_core__Lazy_LazyConst


class tink_core__Future_SyncFuture:
    _hx_class_name = "tink.core._Future.SyncFuture"
    _hx_is_interface = "False"
    __slots__ = ("value",)
    _hx_fields = ["value"]
    _hx_methods = ["getStatus", "handle", "eager"]
    _hx_interfaces = [tink_core__Future_FutureObject]

    def __init__(self,value):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:385
        self.value = value

    def getStatus(self):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:382
        return tink_core_FutureStatus.Ready(self.value)

    def handle(self,cb):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:388
        tink_core__Callback_Callback_Impl_.invoke(cb,tink_core__Lazy_Lazy_Impl_.get(self.value))
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:389
        return None

    def eager(self):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:393
        if (not self.value.isComputed()):
            tink_core__Lazy_Lazy_Impl_.get(self.value)

tink_core__Future_SyncFuture._hx_class = tink_core__Future_SyncFuture


class tink_core__Future_Future_Impl_:
    _hx_class_name = "tink.core._Future.Future_Impl_"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["NOISE", "NULL", "NEVER", "get_status", "_new", "handle", "eager", "noise", "first", "map", "flatMap", "next", "gather", "merge", "flatten", "neverToAny", "ofAny", "asPromise", "ofMany", "inParallel", "inSequence", "many", "processMany", "lazy", "sync", "isFuture", "make", "irreversible", "or", "either", "and", "_tryFailingFlatMap", "_tryFlatMap", "_tryFailingMap", "_tryMap", "_flatMap", "_map", "trigger", "delay"]
    status = None

    @staticmethod
    def get_status(this1):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:36
        return this1.getStatus()

    @staticmethod
    def _new(wakeup):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:47
        this1 = tink_core__Future_SuspendableFuture(wakeup)
        return this1

    @staticmethod
    def handle(this1,callback):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:56
        return this1.handle(callback)

    @staticmethod
    def eager(this1):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:64
        this1.eager()
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:65
        return this1

    @staticmethod
    def noise(this1):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:70
        if (this1.getStatus().index == 4):
            return tink_core__Future_Future_Impl_.NEVER
        else:
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:71
            def _hx_local_1():
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:71
                def _hx_local_0(_):
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:71
                    return None
                return tink_core__Future_Future_Impl_.map(this1,_hx_local_0)
            return _hx_local_1()

    @staticmethod
    def first(this1,that):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:77
        _g = this1
        _g1 = _g.getStatus()
        tmp = _g1.index
        if (tmp == 3):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:80
            _g2 = _g1.params[0]
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:77
            _g1 = that.getStatus()
            tmp = _g1.index
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:78
            if (tmp == 3):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:81
                _g2 = _g1.params[0]
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:80
                v = _g
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:82
                return v
            elif (tmp == 4):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:80
                v = _g
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:82
                return v
            else:
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:80
                v = _g
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:82
                return v
        elif (tmp == 4):
            v = that
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:82
            return v
        else:
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:77
            _g1 = that.getStatus()
            tmp = _g1.index
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:78
            if (tmp == 3):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:81
                _g2 = _g1.params[0]
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:78
                v = that
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:82
                return v
            elif (tmp == 4):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:80
                v = _g
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:82
                return v
            else:
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:84
                def _hx_local_1():
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:84
                    def _hx_local_0(fire):
                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:84
                        return tink_core__Callback_LinkPair(this1.handle(fire),that.handle(fire))
                    return tink_core__Future_SuspendableFuture(_hx_local_0)
                return _hx_local_1()

    @staticmethod
    def map(this1,f,gather = None):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:92
        _g = this1.getStatus()
        tmp = _g.index
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:94
        if (tmp == 3):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:94
            l = _g.params[0]
            this2 = l
            f1 = f
            def _hx_local_1():
                def _hx_local_0():
                    return f1(this2.get())
                return tink_core__Future_SyncFuture(tink_core__Lazy_LazyFunc(_hx_local_0,this2))
            return _hx_local_1()
        elif (tmp == 4):
            return tink_core__Future_Future_Impl_.NEVER
        else:
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:95
            def _hx_local_5():
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:95
                def _hx_local_4(fire):
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:95
                    def _hx_local_3():
                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:95
                        def _hx_local_2(v):
                            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:95
                            fire(f(v))
                        return this1.handle(_hx_local_2)
                    return _hx_local_3()
                return tink_core__Future_SuspendableFuture(_hx_local_4)
            return _hx_local_5()

    @staticmethod
    def flatMap(this1,next,gather = None):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:103
        _g = this1.getStatus()
        tmp = _g.index
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:105
        if (tmp == 3):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:105
            l = _g.params[0]
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:106
            def _hx_local_3():
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:106
                def _hx_local_2(fire):
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:106
                    def _hx_local_1():
                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:106
                        def _hx_local_0(v):
                            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:106
                            fire(v)
                        return next(tink_core__Lazy_Lazy_Impl_.get(l)).handle(_hx_local_0)
                    return _hx_local_1()
                return tink_core__Future_SuspendableFuture(_hx_local_2)
            return _hx_local_3()
        elif (tmp == 4):
            return tink_core__Future_Future_Impl_.NEVER
        else:
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:108
            def _hx_local_6():
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:108
                def _hx_local_5(_hx_yield):
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:109
                    inner = tink_core_CallbackLinkRef()
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:110
                    def _hx_local_4(v):
                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:110
                        outer = next(v).handle(_hx_yield)
                        inner.link = outer
                    outer = this1.handle(_hx_local_4)
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:111
                    return tink_core__Callback_LinkPair(outer,inner)
                return tink_core__Future_SuspendableFuture(_hx_local_5)
            return _hx_local_6()

    @staticmethod
    def next(this1,n):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:120
        return tink_core__Future_Future_Impl_.flatMap(this1,n)

    @staticmethod
    def gather(this1):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:124
        return this1

    @staticmethod
    def merge(this1,that,combine):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:130
        _g = this1.getStatus()
        _g1 = that.getStatus()
        if (_g.index == 4):
            return tink_core__Future_Future_Impl_.NEVER
        elif (_g1.index == 4):
            return tink_core__Future_Future_Impl_.NEVER
        else:
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:133
            def _hx_local_2():
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:133
                def _hx_local_1(_hx_yield):
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:135
                    def _hx_local_0(v = None):
                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:135
                        _g = this1.getStatus()
                        _g1 = that.getStatus()
                        if (_g.index == 3):
                            if (_g1.index == 3):
                                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:136
                                b = _g1.params[0]
                                a = _g.params[0]
                                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:137
                                _hx_yield(combine(tink_core__Lazy_Lazy_Impl_.get(a),tink_core__Lazy_Lazy_Impl_.get(b)))
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:134
                    check = _hx_local_0
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:141
                    return tink_core__Callback_LinkPair(this1.handle(check),that.handle(check))
                return tink_core__Future_SuspendableFuture(_hx_local_1)
            return _hx_local_2()

    @staticmethod
    def flatten(f):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:150
        def _hx_local_1():
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:150
            def _hx_local_0(v):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:150
                return v
            return tink_core__Future_Future_Impl_.flatMap(f,_hx_local_0)
        return _hx_local_1()

    @staticmethod
    def neverToAny(l):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:162
        return l

    @staticmethod
    def ofAny(v):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:165
        return tink_core__Future_SyncFuture(tink_core__Lazy_LazyConst(v))

    @staticmethod
    def asPromise(s):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:171
        return s

    @staticmethod
    def ofMany(futures,gather = None):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:175
        return tink_core__Future_Future_Impl_.inSequence(futures)

    @staticmethod
    def inParallel(futures,concurrency = None):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:183
        return tink_core__Future_Future_Impl_.many(futures,concurrency)

    @staticmethod
    def inSequence(futures):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:190
        return tink_core__Future_Future_Impl_.many(futures,1)

    @staticmethod
    def many(a,concurrency = None):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:193
        def _hx_local_1():
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:193
            def _hx_local_0(o):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:193
                return tink_core_OutcomeTools.orNull(o)
            return tink_core__Future_Future_Impl_.processMany(a,concurrency,tink_core_Outcome.Success,_hx_local_0)
        return _hx_local_1()

    @staticmethod
    def processMany(a,concurrency = None,fn = None,lift = None):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:196
        if (len(a) == 0):
            return tink_core__Future_SyncFuture(tink_core__Lazy_LazyConst(lift(tink_core_Outcome.Success([]))))
        else:
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:198
            def _hx_local_11(_hx_yield):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:199
                links = list()
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:200
                _g = []
                _g1 = 0
                while (_g1 < len(a)):
                    x = (a[_g1] if _g1 >= 0 and _g1 < len(a) else None)
                    _g1 = (_g1 + 1)
                    _g.append(None)
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:199
                ret = _g
                index = 0
                pending = 0
                done = False
                concurrency1 = None
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:204
                if (concurrency is None):
                    concurrency1 = len(a)
                else:
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:206
                    v = concurrency
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:199
                    concurrency1 = (1 if ((v < 1)) else (len(a) if ((v > len(a))) else v))
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:219
                def _hx_local_1():
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:219
                    nonlocal done
                    if (index == len(ret)):
                        if (pending == 0):
                            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:221
                            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:221
                            v = lift(tink_core_Outcome.Success(ret))
                            done = True
                            _hx_yield(v)
                            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:222
                            return True
                        else:
                            return False
                    else:
                        return False
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:217
                fireWhenReady = _hx_local_1
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:227
                step = None
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:228
                def _hx_local_10():
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:228
                    nonlocal pending
                    nonlocal index
                    if ((not done) and (not fireWhenReady())):
                        while (index < len(ret)):
                            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:231
                            index = (index + 1)
                            index1 = [(index - 1)]
                            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:232
                            p = python_internal_ArrayImpl._get(a, (index1[0] if 0 < len(index1) else None))
                            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:234
                            def _hx_local_5(index):
                                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:234
                                def _hx_local_3(o):
                                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:234
                                    nonlocal done
                                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:235
                                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:235
                                    _g = fn(o)
                                    check = _g.index
                                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:236
                                    if (check == 0):
                                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:236
                                        v = _g.params[0]
                                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:237
                                        python_internal_ArrayImpl._set(ret, (index[0] if 0 < len(index) else None), v)
                                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:238
                                        fireWhenReady()
                                    elif (check == 1):
                                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:239
                                        e = _g.params[0]
                                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:240
                                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:240
                                        _g = 0
                                        while (_g < len(links)):
                                            l = (links[_g] if _g >= 0 and _g < len(links) else None)
                                            _g = (_g + 1)
                                            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:241
                                            if (l is not None):
                                                l.cancel()
                                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:242
                                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:242
                                        v = lift(tink_core_Outcome.Failure(e))
                                        done = True
                                        _hx_yield(v)
                                    else:
                                        pass
                                return _hx_local_3
                            check = [_hx_local_5(index1)]
                            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:245
                            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:245
                            _g = p.getStatus()
                            if (_g.index == 3):
                                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:246
                                _hx_tmp = None
                                _hx_tmp = tink_core__Lazy_Lazy_Impl_.get(_g.params[0])
                                v = _hx_tmp
                                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:247
                                (check[0] if 0 < len(check) else None)(v)
                                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:248
                                if (not done):
                                    continue
                            else:
                                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:250
                                pending = (pending + 1)
                                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:251
                                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:252
                                def _hx_local_9(check):
                                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:252
                                    def _hx_local_7(o):
                                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:252
                                        nonlocal pending
                                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:253
                                        pending = (pending - 1)
                                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:254
                                        (check[0] if 0 < len(check) else None)(o)
                                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:255
                                        if (not done):
                                            step()
                                    return _hx_local_7
                                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:251
                                x = p.handle(_hx_local_9(check))
                                links.append(x)
                            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:259
                            break
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:227
                step = _hx_local_10
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:262
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:262
                _g = 0
                _g1 = concurrency1
                while (_g < _g1):
                    i = _g
                    _g = (_g + 1)
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:263
                    step()
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:265
                return tink_core__Callback_CallbackLink_Impl_.fromMany(links)
            this1 = tink_core__Future_SuspendableFuture(_hx_local_11)
            return this1

    @staticmethod
    def lazy(l):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:272
        return tink_core__Future_SyncFuture(l)

    @staticmethod
    def sync(v):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:279
        return tink_core__Future_SyncFuture(tink_core__Lazy_LazyConst(v))

    @staticmethod
    def isFuture(maybeFuture):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:282
        return Std.isOfType(maybeFuture,tink_core__Future_FutureObject)

    @staticmethod
    def make(init,lazy = None):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:286
        if (lazy is None):
            lazy = False
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:287
        ret = tink_core__Future_Future_Impl_.irreversible(init)
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:288
        if lazy:
            return ret
        else:
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:288
            ret.eager()
            return ret

    @staticmethod
    def irreversible(init):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:297
        def _hx_local_1():
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:297
            def _hx_local_0(_hx_yield):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:297
                init(_hx_yield)
                return None
            return tink_core__Future_SuspendableFuture(_hx_local_0)
        return _hx_local_1()

    @staticmethod
    def _hx_or(a,b):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:303
        return tink_core__Future_Future_Impl_.first(a,b)

    @staticmethod
    def either(a,b):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:309
        return tink_core__Future_Future_Impl_.first(tink_core__Future_Future_Impl_.map(a,haxe_ds_Either.Left),tink_core__Future_Future_Impl_.map(b,haxe_ds_Either.Right))

    @staticmethod
    def _hx_and(a,b):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:315
        def _hx_local_1():
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:315
            def _hx_local_0(a,b):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:315
                this1 = tink_core_MPair(a,b)
                return this1
            return tink_core__Future_Future_Impl_.merge(a,b,_hx_local_0)
        return _hx_local_1()

    @staticmethod
    def _tryFailingFlatMap(f,_hx_map):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:318
        def _hx_local_1():
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:318
            def _hx_local_0(o):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:318
                tmp = o.index
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:319
                if (tmp == 0):
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:319
                    d = o.params[0]
                    return _hx_map(d)
                elif (tmp == 1):
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:320
                    f = o.params[0]
                    return tink_core__Future_SyncFuture(tink_core__Lazy_LazyConst(tink_core_Outcome.Failure(f)))
                else:
                    pass
            return tink_core__Future_Future_Impl_.flatMap(f,_hx_local_0)
        return _hx_local_1()

    @staticmethod
    def _tryFlatMap(f,_hx_map):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:324
        def _hx_local_1():
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:324
            def _hx_local_0(o):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:324
                tmp = o.index
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:325
                if (tmp == 0):
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:325
                    d = o.params[0]
                    return tink_core__Future_Future_Impl_.map(_hx_map(d),tink_core_Outcome.Success)
                elif (tmp == 1):
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:326
                    f = o.params[0]
                    return tink_core__Future_SyncFuture(tink_core__Lazy_LazyConst(tink_core_Outcome.Failure(f)))
                else:
                    pass
            return tink_core__Future_Future_Impl_.flatMap(f,_hx_local_0)
        return _hx_local_1()

    @staticmethod
    def _tryFailingMap(f,_hx_map):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:330
        def _hx_local_1():
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:330
            def _hx_local_0(o):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:330
                return tink_core_OutcomeTools.flatMap(o,tink_core__Outcome_OutcomeMapper_Impl_.withSameError(_hx_map))
            return tink_core__Future_Future_Impl_.map(f,_hx_local_0)
        return _hx_local_1()

    @staticmethod
    def _tryMap(f,_hx_map):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:333
        def _hx_local_1():
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:333
            def _hx_local_0(o):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:333
                return tink_core_OutcomeTools.map(o,_hx_map)
            return tink_core__Future_Future_Impl_.map(f,_hx_local_0)
        return _hx_local_1()

    @staticmethod
    def _flatMap(f,_hx_map):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:336
        return tink_core__Future_Future_Impl_.flatMap(f,_hx_map)

    @staticmethod
    def _map(f,_hx_map):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:339
        return tink_core__Future_Future_Impl_.map(f,_hx_map)

    @staticmethod
    def trigger():
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:346
        return tink_core_FutureTrigger()

    @staticmethod
    def delay(ms,value):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:350
        def _hx_local_1(cb):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:350
            def _hx_local_0():
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:350
                cb(tink_core__Lazy_Lazy_Impl_.get(value))
            haxe_Timer.delay(_hx_local_0,ms)
        this1 = tink_core__Future_Future_Impl_.irreversible(_hx_local_1)
        this1.eager()
        return this1
tink_core__Future_Future_Impl_._hx_class = tink_core__Future_Future_Impl_

class tink_core_FutureStatus(Enum):
    __slots__ = ()
    _hx_class_name = "tink.core.FutureStatus"
    _hx_constructs = ["Suspended", "Awaited", "EagerlyAwaited", "Ready", "NeverEver"]

    @staticmethod
    def Ready(result):
        return tink_core_FutureStatus("Ready", 3, (result,))
tink_core_FutureStatus.Suspended = tink_core_FutureStatus("Suspended", 0, ())
tink_core_FutureStatus.Awaited = tink_core_FutureStatus("Awaited", 1, ())
tink_core_FutureStatus.EagerlyAwaited = tink_core_FutureStatus("EagerlyAwaited", 2, ())
tink_core_FutureStatus.NeverEver = tink_core_FutureStatus("NeverEver", 4, ())
tink_core_FutureStatus._hx_class = tink_core_FutureStatus


class tink_core_FutureTrigger:
    _hx_class_name = "tink.core.FutureTrigger"
    _hx_is_interface = "False"
    __slots__ = ("status", "list")
    _hx_fields = ["status", "list"]
    _hx_methods = ["getStatus", "handle", "eager", "asFuture", "trigger"]
    _hx_interfaces = [tink_core__Future_FutureObject]

    def __init__(self):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:399
        self.status = tink_core_FutureStatus.Awaited
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:403
        self.list = tink_core_CallbackList(True)

    def getStatus(self):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:406
        return self.status

    def handle(self,callback):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:409
        _g = self.status
        if (_g.index == 3):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:410
            result = _g.params[0]
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:411
            tink_core__Callback_Callback_Impl_.invoke(callback,tink_core__Lazy_Lazy_Impl_.get(result))
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:412
            return None
        else:
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:413
            v = _g
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:414
            _this = self.list
            if (_this.disposeHandlers is None):
                return None
            else:
                node = tink_core__Callback_ListCell(callback,_this)
                _this1 = _this.cells
                _this1.append(node)
                def _hx_local_1():
                    _hx_local_0 = _this.used
                    _this.used = (_this.used + 1)
                    return _hx_local_0
                tmp = (_hx_local_1() == 0)
                if tmp:
                    fn = _this.onfill
                    if (tink_core__Callback_Callback_Impl_.depth < 100):
                        _hx_local_2 = tink_core__Callback_Callback_Impl_
                        _hx_local_3 = _hx_local_2.depth
                        _hx_local_2.depth = (_hx_local_3 + 1)
                        _hx_local_3
                        fn()
                        _hx_local_4 = tink_core__Callback_Callback_Impl_
                        _hx_local_5 = _hx_local_4.depth
                        _hx_local_4.depth = (_hx_local_5 - 1)
                        _hx_local_5
                    else:
                        tink_core__Callback_Callback_Impl_.defer(fn)
                return node

    def eager(self):
        pass

    def asFuture(self):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:420
        return self

    def trigger(self,result):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:426
        _g = self.status
        if (_g.index == 3):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:427
            _g1 = _g.params[0]
            return False
        else:
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:429
            self.status = tink_core_FutureStatus.Ready(tink_core__Lazy_LazyConst(result))
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:430
            self.list.invoke(result)
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:431
            return True

tink_core_FutureTrigger._hx_class = tink_core_FutureTrigger


class tink_core__Future_SuspendableFuture:
    _hx_class_name = "tink.core._Future.SuspendableFuture"
    _hx_is_interface = "False"
    __slots__ = ("callbacks", "status", "link", "wakeup")
    _hx_fields = ["callbacks", "status", "link", "wakeup"]
    _hx_methods = ["getStatus", "trigger", "handle", "arm", "eager"]
    _hx_interfaces = [tink_core__Future_FutureObject]

    def __init__(self,wakeup):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:450
        self.wakeup = None
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:449
        self.link = None
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:447
        self.callbacks = None
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:448
        self.status = tink_core_FutureStatus.Suspended
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:455
        _gthis = self
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:456
        self.wakeup = wakeup
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:457
        self.callbacks = tink_core_CallbackList(True)
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:459
        def _hx_local_0():
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:459
            if (_gthis.status == tink_core_FutureStatus.Awaited):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:460
                _gthis.status = tink_core_FutureStatus.Suspended
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:461
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:461
                this1 = _gthis.link
                if (this1 is not None):
                    this1.cancel()
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:462
                _gthis.link = None
        self.callbacks.ondrain = _hx_local_0
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:464
        def _hx_local_1():
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:464
            if (_gthis.status == tink_core_FutureStatus.Suspended):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:465
                _gthis.status = tink_core_FutureStatus.Awaited
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:466
                _gthis.arm()
        self.callbacks.onfill = _hx_local_1

    def getStatus(self):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:453
        return self.status

    def trigger(self,value):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:471
        _g = self.status
        if (_g.index == 3):
            _g1 = _g.params[0]
        else:
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:474
            self.status = tink_core_FutureStatus.Ready(tink_core__Lazy_LazyConst(value))
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:475
            link = self.link
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:476
            self.link = None
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:477
            self.wakeup = None
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:478
            self.callbacks.invoke(value)
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:479
            if (link is not None):
                link.cancel()

    def handle(self,callback):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:483
        _g = self.status
        if (_g.index == 3):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:484
            result = _g.params[0]
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:485
            tink_core__Callback_Callback_Impl_.invoke(callback,tink_core__Lazy_Lazy_Impl_.get(result))
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:486
            return None
        else:
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:488
            _this = self.callbacks
            if (_this.disposeHandlers is None):
                return None
            else:
                node = tink_core__Callback_ListCell(callback,_this)
                _this1 = _this.cells
                _this1.append(node)
                def _hx_local_1():
                    _hx_local_0 = _this.used
                    _this.used = (_this.used + 1)
                    return _hx_local_0
                tmp = (_hx_local_1() == 0)
                if tmp:
                    fn = _this.onfill
                    if (tink_core__Callback_Callback_Impl_.depth < 100):
                        _hx_local_2 = tink_core__Callback_Callback_Impl_
                        _hx_local_3 = _hx_local_2.depth
                        _hx_local_2.depth = (_hx_local_3 + 1)
                        _hx_local_3
                        fn()
                        _hx_local_4 = tink_core__Callback_Callback_Impl_
                        _hx_local_5 = _hx_local_4.depth
                        _hx_local_4.depth = (_hx_local_5 - 1)
                        _hx_local_5
                    else:
                        tink_core__Callback_Callback_Impl_.defer(fn)
                return node

    def arm(self):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:492
        _gthis = self
        def _hx_local_0(x):
            _gthis.trigger(x)
        self.link = self.wakeup(_hx_local_0)

    def eager(self):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:495
        tmp = self.status.index
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:496
        if (tmp == 0):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:497
            self.status = tink_core_FutureStatus.EagerlyAwaited
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Future.hx:498
            self.arm()
        elif (tmp == 1):
            self.status = tink_core_FutureStatus.EagerlyAwaited
        else:
            pass

tink_core__Future_SuspendableFuture._hx_class = tink_core__Future_SuspendableFuture


class tink_core__Lazy_Lazy_Impl_:
    _hx_class_name = "tink.core._Lazy.Lazy_Impl_"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["NOISE", "NULL", "get_computed", "get", "fromNoise", "ofFunc", "map", "flatMap", "ofConst"]
    computed = None

    @staticmethod
    def get_computed(this1):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Lazy.hx:10
        return this1.isComputed()

    @staticmethod
    def get(this1):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Lazy.hx:13
        this1.compute()
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Lazy.hx:14
        return this1.get()

    @staticmethod
    def fromNoise(l):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Lazy.hx:18
        return l

    @staticmethod
    def ofFunc(f):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Lazy.hx:21
        return tink_core__Lazy_LazyFunc(f)

    @staticmethod
    def map(this1,f):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Lazy.hx:24
        def _hx_local_1():
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Lazy.hx:24
            def _hx_local_0():
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Lazy.hx:24
                return f(this1.get())
            return tink_core__Lazy_LazyFunc(_hx_local_0,this1)
        return _hx_local_1()

    @staticmethod
    def flatMap(this1,f):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Lazy.hx:27
        def _hx_local_1():
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Lazy.hx:27
            def _hx_local_0():
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Lazy.hx:27
                return tink_core__Lazy_Lazy_Impl_.get(f(this1.get()))
            return tink_core__Lazy_LazyFunc(_hx_local_0,this1)
        return _hx_local_1()

    @staticmethod
    def ofConst(c):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Lazy.hx:31
        return tink_core__Lazy_LazyConst(c)
tink_core__Lazy_Lazy_Impl_._hx_class = tink_core__Lazy_Lazy_Impl_


class tink_core__Lazy_LazyFunc:
    _hx_class_name = "tink.core._Lazy.LazyFunc"
    _hx_is_interface = "False"
    __slots__ = ("f", "_hx_from", "result", "busy")
    _hx_fields = ["f", "from", "result", "busy"]
    _hx_methods = ["underlying", "isComputed", "get", "compute"]
    _hx_interfaces = [tink_core__Lazy_LazyObject]

    def __init__(self,f,_hx_from = None):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Lazy.hx:67
        self.result = None
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Lazy.hx:68
        self.busy = False
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Lazy.hx:71
        self.f = f
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Lazy.hx:72
        self._hx_from = _hx_from

    def underlying(self):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Lazy.hx:76
        return self._hx_from

    def isComputed(self):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Lazy.hx:79
        return (self.f is None)

    def get(self):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Lazy.hx:82
        return self.result

    def compute(self):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Lazy.hx:85
        if self.busy:
            raise haxe_Exception.thrown(tink_core_TypedError(None,"circular lazyness",_hx_AnonObject({'fileName': "tink/core/Lazy.hx", 'lineNumber': 85, 'className': "tink.core._Lazy.LazyFunc", 'methodName': "compute"})))
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Lazy.hx:86
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Lazy.hx:86
        _g = self.f
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Lazy.hx:87
        if (_g is not None):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Lazy.hx:88
            v = _g
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Lazy.hx:89
            self.busy = True
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Lazy.hx:90
            self.f = None
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Lazy.hx:91
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Lazy.hx:91
            _g = self._hx_from
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Lazy.hx:92
            if (_g is not None):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Lazy.hx:93
                cur = _g
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Lazy.hx:94
                self._hx_from = None
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Lazy.hx:95
                stack = []
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Lazy.hx:96
                while ((cur is not None) and (not cur.isComputed())):
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Lazy.hx:97
                    stack.append(cur)
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Lazy.hx:98
                    cur = cur.underlying()
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Lazy.hx:100
                stack.reverse()
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Lazy.hx:101
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Lazy.hx:101
                _g = 0
                while (_g < len(stack)):
                    c = (stack[_g] if _g >= 0 and _g < len(stack) else None)
                    _g = (_g + 1)
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Lazy.hx:102
                    c.compute()
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Lazy.hx:106
            self.result = v()
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Lazy.hx:107
            self.busy = False

tink_core__Lazy_LazyFunc._hx_class = tink_core__Lazy_LazyFunc


class tink_core_NamedWith:
    _hx_class_name = "tink.core.NamedWith"
    _hx_is_interface = "False"
    __slots__ = ("name", "value")
    _hx_fields = ["name", "value"]

    def __init__(self,name,value):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Named.hx:12
        self.name = name
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Named.hx:13
        self.value = value

tink_core_NamedWith._hx_class = tink_core_NamedWith


class tink_core__Noise_Noise_Impl_:
    _hx_class_name = "tink.core._Noise.Noise_Impl_"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["Noise", "ofAny"]

    @staticmethod
    def ofAny(t):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Noise.hx:6
        return None
tink_core__Noise_Noise_Impl_._hx_class = tink_core__Noise_Noise_Impl_


class tink_core_OptionTools:
    _hx_class_name = "tink.core.OptionTools"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["force", "sure", "toOutcome", "or", "orTry", "orNull", "filter", "satisfies", "equals", "map", "flatMap", "iterator", "toArray"]

    @staticmethod
    def force(o,pos = None):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Option.hx:9
        if (o.index == 0):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Option.hx:9
            v = o.params[0]
            return v
        else:
            raise haxe_Exception.thrown(tink_core_TypedError(404,"Some value expected but none found",pos))

    @staticmethod
    def sure(o,pos = None):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Option.hx:15
        if (o.index == 0):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Option.hx:16
            v = o.params[0]
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Option.hx:17
            return v
        else:
            raise haxe_Exception.thrown(tink_core_TypedError(404,"Some value expected but none found",pos))

    @staticmethod
    def toOutcome(o,pos = None):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Option.hx:27
        tmp = o.index
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Option.hx:28
        if (tmp == 0):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Option.hx:28
            value = o.params[0]
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Option.hx:29
            return tink_core_Outcome.Success(value)
        elif (tmp == 1):
            return tink_core_Outcome.Failure(tink_core_TypedError(404,((("Some value expected but none found in " + HxOverrides.stringOrNull(pos.fileName)) + "@line ") + Std.string(pos.lineNumber)),_hx_AnonObject({'fileName': "tink/core/Option.hx", 'lineNumber': 31, 'className': "tink.core.OptionTools", 'methodName': "toOutcome"})))
        else:
            pass

    @staticmethod
    def _hx_or(o,l):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Option.hx:39
        if (o.index == 0):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Option.hx:40
            v = o.params[0]
            return v
        else:
            return tink_core__Lazy_Lazy_Impl_.get(l)

    @staticmethod
    def orTry(o,fallback):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Option.hx:48
        if (o.index == 0):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Option.hx:49
            v = o.params[0]
            return o
        else:
            return tink_core__Lazy_Lazy_Impl_.get(fallback)

    @staticmethod
    def orNull(o):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Option.hx:57
        if (o.index == 0):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Option.hx:58
            v = o.params[0]
            return v
        else:
            return None

    @staticmethod
    def filter(o,f):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Option.hx:66
        if (o.index == 0):
            if (f(o.params[0]) == False):
                return haxe_ds_Option._hx_None
            else:
                return o
        else:
            return o

    @staticmethod
    def satisfies(o,f):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Option.hx:75
        if (o.index == 0):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Option.hx:76
            v = o.params[0]
            return f(v)
        else:
            return False

    @staticmethod
    def equals(o,v):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Option.hx:84
        if (o.index == 0):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Option.hx:84
            v1 = o.params[0]
            return HxOverrides.eq(v1,v)
        else:
            return False

    @staticmethod
    def map(o,f):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Option.hx:91
        if (o.index == 0):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Option.hx:92
            v = o.params[0]
            return haxe_ds_Option.Some(f(v))
        else:
            return haxe_ds_Option._hx_None

    @staticmethod
    def flatMap(o,f):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Option.hx:101
        if (o.index == 0):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Option.hx:102
            v = o.params[0]
            return f(v)
        else:
            return haxe_ds_Option._hx_None

    @staticmethod
    def iterator(o):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Option.hx:111
        return tink_core_OptionIter(o)

    @staticmethod
    def toArray(o):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Option.hx:118
        if (o.index == 0):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Option.hx:119
            v = o.params[0]
            return [v]
        else:
            return []
tink_core_OptionTools._hx_class = tink_core_OptionTools


class tink_core_OptionIter:
    _hx_class_name = "tink.core.OptionIter"
    _hx_is_interface = "False"
    __slots__ = ("value", "alive")
    _hx_fields = ["value", "alive"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,o):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Option.hx:126
        self.value = None
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Option.hx:127
        self.alive = True
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Option.hx:130
        if (o.index == 0):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Option.hx:131
            v = o.params[0]
            self.value = v
        else:
            self.alive = False

    def hasNext(self):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Option.hx:136
        return self.alive

    def next(self):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Option.hx:139
        self.alive = False
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Option.hx:141
        return self.value

tink_core_OptionIter._hx_class = tink_core_OptionIter

class tink_core_Outcome(Enum):
    __slots__ = ()
    _hx_class_name = "tink.core.Outcome"
    _hx_constructs = ["Success", "Failure"]

    @staticmethod
    def Success(data):
        return tink_core_Outcome("Success", 0, (data,))

    @staticmethod
    def Failure(failure):
        return tink_core_Outcome("Failure", 1, (failure,))
tink_core_Outcome._hx_class = tink_core_Outcome


class tink_core_OutcomeTools:
    _hx_class_name = "tink.core.OutcomeTools"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["sure", "toOption", "orNull", "orUse", "or", "orTry", "equals", "map", "isSuccess", "flatMap", "swap", "next", "attempt", "flatten"]

    @staticmethod
    def sure(outcome):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:24
        tmp = outcome.index
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:25
        if (tmp == 0):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:25
            data = outcome.params[0]
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:26
            return data
        elif (tmp == 1):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:27
            failure = outcome.params[0]
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:28
            _g = tink_core_TypedError.asError(failure)
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:29
            if (_g is None):
                raise haxe_Exception.thrown(failure)
            else:
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:30
                e = _g
                return e.throwSelf()
        else:
            pass

    @staticmethod
    def toOption(outcome):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:39
        tmp = outcome.index
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:40
        if (tmp == 0):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:40
            data = outcome.params[0]
            return haxe_ds_Option.Some(data)
        elif (tmp == 1):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:41
            _g = outcome.params[0]
            return haxe_ds_Option._hx_None
        else:
            pass

    @staticmethod
    def orNull(outcome):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:49
        tmp = outcome.index
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:50
        if (tmp == 0):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:50
            data = outcome.params[0]
            return data
        elif (tmp == 1):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:51
            _g = outcome.params[0]
            return None
        else:
            pass

    @staticmethod
    def orUse(outcome,fallback):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:56
        return tink_core_OutcomeTools._hx_or(outcome,fallback)

    @staticmethod
    def _hx_or(outcome,fallback):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:63
        tmp = outcome.index
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:64
        if (tmp == 0):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:64
            data = outcome.params[0]
            return data
        elif (tmp == 1):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:65
            _g = outcome.params[0]
            return tink_core__Lazy_Lazy_Impl_.get(fallback)
        else:
            pass

    @staticmethod
    def orTry(outcome,fallback):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:73
        tmp = outcome.index
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:74
        if (tmp == 0):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:74
            _g = outcome.params[0]
            return outcome
        elif (tmp == 1):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:75
            _g = outcome.params[0]
            return tink_core__Lazy_Lazy_Impl_.get(fallback)
        else:
            pass

    @staticmethod
    def equals(outcome,to):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:82
        tmp = outcome.index
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:83
        if (tmp == 0):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:83
            data = outcome.params[0]
            return HxOverrides.eq(data,to)
        elif (tmp == 1):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:84
            _g = outcome.params[0]
            return False
        else:
            pass

    @staticmethod
    def map(outcome,transform):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:92
        tmp = outcome.index
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:93
        if (tmp == 0):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:93
            a = outcome.params[0]
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:94
            return tink_core_Outcome.Success(transform(a))
        elif (tmp == 1):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:95
            f = outcome.params[0]
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:96
            return tink_core_Outcome.Failure(f)
        else:
            pass

    @staticmethod
    def isSuccess(outcome):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:104
        if (outcome.index == 0):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:105
            _g = outcome.params[0]
            return True
        else:
            return False

    @staticmethod
    def flatMap(o,mapper):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:115
        return tink_core__Outcome_OutcomeMapper_Impl_.apply(mapper,o)

    @staticmethod
    def swap(outcome,v):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:123
        tmp = outcome.index
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:124
        if (tmp == 0):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:124
            a = outcome.params[0]
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:125
            return tink_core_Outcome.Success(v)
        elif (tmp == 1):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:126
            f = outcome.params[0]
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:127
            return tink_core_Outcome.Failure(f)
        else:
            pass

    @staticmethod
    def next(outcome,f):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:131
        tmp = outcome.index
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:132
        if (tmp == 0):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:132
            v = outcome.params[0]
            return f(v)
        elif (tmp == 1):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:133
            e = outcome.params[0]
            return tink_core__Future_SyncFuture(tink_core__Lazy_LazyConst(tink_core_Outcome.Failure(e)))
        else:
            pass

    @staticmethod
    def attempt(f,report):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:142
        try:
            return tink_core_Outcome.Success(f())
        except BaseException as _g:
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:143
            None
            e = haxe_Exception.caught(_g).unwrap()
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:144
            return tink_core_Outcome.Failure(report(e))

    @staticmethod
    def flatten(o):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:147
        tmp = o.index
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:149
        if (tmp == 0):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:149
            _g = o.params[0]
            tmp = _g.index
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:148
            if (tmp == 0):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:148
                d = _g.params[0]
                return tink_core_Outcome.Success(d)
            elif (tmp == 1):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:149
                f = _g.params[0]
                return tink_core_Outcome.Failure(f)
            else:
                pass
        elif (tmp == 1):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:149
            f = o.params[0]
            return tink_core_Outcome.Failure(f)
        else:
            pass
tink_core_OutcomeTools._hx_class = tink_core_OutcomeTools


class tink_core__Outcome_OutcomeMapper_Impl_:
    _hx_class_name = "tink.core._Outcome.OutcomeMapper_Impl_"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["_new", "apply", "withSameError", "withEitherError"]

    @staticmethod
    def _new(f):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:154
        this1 = _hx_AnonObject({'f': f})
        return this1

    @staticmethod
    def apply(this1,o):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:156
        return this1.f(o)

    @staticmethod
    def withSameError(f):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:159
        def _hx_local_1():
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:160
            def _hx_local_0(o):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:160
                tmp = o.index
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:161
                if (tmp == 0):
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:161
                    d = o.params[0]
                    return f(d)
                elif (tmp == 1):
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:162
                    f1 = o.params[0]
                    return tink_core_Outcome.Failure(f1)
                else:
                    pass
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:159
            return tink_core__Outcome_OutcomeMapper_Impl_._new(_hx_local_0)
        return _hx_local_1()

    @staticmethod
    def withEitherError(f):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:168
        def _hx_local_1():
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:169
            def _hx_local_0(o):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:169
                tmp = o.index
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:170
                if (tmp == 0):
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:170
                    d = o.params[0]
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:171
                    _g = f(d)
                    tmp = _g.index
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:172
                    if (tmp == 0):
                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:172
                        d = _g.params[0]
                        return tink_core_Outcome.Success(d)
                    elif (tmp == 1):
                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:173
                        f1 = _g.params[0]
                        return tink_core_Outcome.Failure(haxe_ds_Either.Right(f1))
                    else:
                        pass
                elif (tmp == 1):
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:175
                    f1 = o.params[0]
                    return tink_core_Outcome.Failure(haxe_ds_Either.Left(f1))
                else:
                    pass
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Outcome.hx:168
            return tink_core__Outcome_OutcomeMapper_Impl_._new(_hx_local_0)
        return _hx_local_1()
tink_core__Outcome_OutcomeMapper_Impl_._hx_class = tink_core__Outcome_OutcomeMapper_Impl_


class tink_core__Pair_Pair_Impl_:
    _hx_class_name = "tink.core._Pair.Pair_Impl_"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["_new", "get_a", "get_b", "toBool", "isNil", "nil"]
    a = None
    b = None

    @staticmethod
    def _new(a,b):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Pair.hx:9
        this1 = tink_core_MPair(a,b)
        return this1

    @staticmethod
    def get_a(this1):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Pair.hx:11
        return this1.a

    @staticmethod
    def get_b(this1):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Pair.hx:12
        return this1.b

    @staticmethod
    def toBool(this1):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Pair.hx:15
        return (this1 is not None)

    @staticmethod
    def isNil(this1):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Pair.hx:18
        return (this1 is None)

    @staticmethod
    def nil():
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Pair.hx:21
        return None
tink_core__Pair_Pair_Impl_._hx_class = tink_core__Pair_Pair_Impl_


class tink_core_MPair:
    _hx_class_name = "tink.core.MPair"
    _hx_is_interface = "False"
    __slots__ = ("a", "b")
    _hx_fields = ["a", "b"]

    def __init__(self,a,b):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Pair.hx:28
        self.a = a
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Pair.hx:29
        self.b = b

tink_core_MPair._hx_class = tink_core_MPair


class tink_core__Progress_ProgressValue_Impl_:
    _hx_class_name = "tink.core._Progress.ProgressValue_Impl_"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["ZERO", "_new", "normalize", "get_value", "get_total"]
    value = None
    total = None

    @staticmethod
    def _new(value,total):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:155
        this1 = tink_core_MPair(value,total)
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:154
        this2 = this1
        return this2

    @staticmethod
    def normalize(this1):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:161
        o = this1.b
        if (o.index == 0):
            v = o.params[0]
            return haxe_ds_Option.Some((this1.a / v))
        else:
            return haxe_ds_Option._hx_None

    @staticmethod
    def get_value(this1):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:164
        return this1.a

    @staticmethod
    def get_total(this1):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:167
        return this1.b
tink_core__Progress_ProgressValue_Impl_._hx_class = tink_core__Progress_ProgressValue_Impl_


class tink_core__Progress_Progress_Impl_:
    _hx_class_name = "tink.core._Progress.Progress_Impl_"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["INIT", "listen", "handle", "trigger", "make", "map", "asFuture", "promise", "flatten", "future", "next"]

    @staticmethod
    def listen(this1,cb):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:18
        return this1.progressed.listen(cb)

    @staticmethod
    def handle(this1,cb):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:21
        return this1.result.handle(cb)

    @staticmethod
    def trigger():
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:24
        return tink_core_ProgressTrigger()

    @staticmethod
    def make(f):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:28
        def _hx_local_4():
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:28
            def _hx_local_3(fire):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:28
                def _hx_local_2():
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:29
                    def _hx_local_0(value,total):
                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:29
                        fire1 = fire
                        this1 = tink_core_MPair(value,total)
                        this2 = this1
                        fire1(tink_core_ProgressStatus.InProgress(this2))
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:30
                    def _hx_local_1(result):
                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:30
                        fire(tink_core_ProgressStatus.Finished(result))
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:28
                    return f(_hx_local_0,_hx_local_1)
                return _hx_local_2()
            return tink_core__Progress_SuspendableProgress(_hx_local_3)
        return _hx_local_4()

    @staticmethod
    def map(this1,f):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:34
        def _hx_local_2():
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:34
            def _hx_local_0(s):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:34
                return tink_core_ProgressStatusTools.map(s,f)
            def _hx_local_1():
                return tink_core_ProgressStatusTools.map(this1.getStatus(),f)
            return tink_core__Progress_ProgressObject(tink_core__Signal_Signal_Impl_.map(this1.changed,_hx_local_0),_hx_local_1)
        return _hx_local_2()

    @staticmethod
    def asFuture(this1):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:38
        return this1.result

    @staticmethod
    def promise(v):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:42
        def _hx_local_4():
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:42
            def _hx_local_3(fire):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:43
                inner = tink_core_CallbackLinkRef()
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:44
                def _hx_local_2():
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:44
                    def _hx_local_1(o):
                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:44
                        this1 = o.index
                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:45
                        if (this1 == 0):
                            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:45
                            p = o.params[0]
                            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:46
                            def _hx_local_0(s):
                                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:46
                                fire(tink_core_ProgressStatusTools.map(s,tink_core_Outcome.Success))
                            this1 = p.changed.listen(_hx_local_0)
                            inner.link = this1
                        elif (this1 == 1):
                            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:47
                            e = o.params[0]
                            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:48
                            fire(tink_core_ProgressStatus.Finished(tink_core_Outcome.Failure(e)))
                        else:
                            pass
                    return tink_core__Callback_LinkPair(v.handle(_hx_local_1),inner)
                return _hx_local_2()
            return tink_core__Progress_SuspendableProgress(_hx_local_3)
        return _hx_local_4()

    @staticmethod
    def flatten(v):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:54
        def _hx_local_1():
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:54
            def _hx_local_0(o):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:54
                tmp = o.index
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:56
                if (tmp == 0):
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:56
                    _g = o.params[0]
                    tmp = _g.index
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:55
                    if (tmp == 0):
                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:55
                        v = _g.params[0]
                        return tink_core_Outcome.Success(v)
                    elif (tmp == 1):
                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:56
                        e = _g.params[0]
                        return tink_core_Outcome.Failure(e)
                    else:
                        pass
                elif (tmp == 1):
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:56
                    e = o.params[0]
                    return tink_core_Outcome.Failure(e)
                else:
                    pass
            return tink_core__Progress_Progress_Impl_.map(tink_core__Progress_Progress_Impl_.promise(v),_hx_local_0)
        return _hx_local_1()

    @staticmethod
    def future(v):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:61
        def _hx_local_3():
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:61
            def _hx_local_2(fire):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:62
                inner = tink_core_CallbackLinkRef()
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:63
                def _hx_local_1():
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:63
                    def _hx_local_0(p):
                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:63
                        this1 = p.changed.listen(fire)
                        inner.link = this1
                    return tink_core__Callback_LinkPair(v.handle(_hx_local_0),inner)
                return _hx_local_1()
            return tink_core__Progress_SuspendableProgress(_hx_local_2)
        return _hx_local_3()

    @staticmethod
    def next(this1,f):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:67
        return tink_core__Future_Future_Impl_.flatMap(this1.result,f)
tink_core__Progress_Progress_Impl_._hx_class = tink_core__Progress_Progress_Impl_


class tink_core__Progress_ProgressObject:
    _hx_class_name = "tink.core._Progress.ProgressObject"
    _hx_is_interface = "False"
    __slots__ = ("getStatus", "changed", "progressed", "result")
    _hx_fields = ["getStatus", "changed", "progressed", "result"]
    _hx_methods = ["get_status"]

    def __init__(self,changed,getStatus):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:103
        self.result = None
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:102
        self.progressed = None
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:99
        self.getStatus = None
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:106
        self.changed = changed
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:107
        def _hx_local_2(fire):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:107
            def _hx_local_1():
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:107
                def _hx_local_0(s):
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:107
                    if (s.index == 0):
                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:108
                        v = s.params[0]
                        fire(v)
                return changed.listen(_hx_local_0)
            return _hx_local_1()
        this1 = tink_core__Signal_Suspendable(_hx_local_2,None)
        self.progressed = this1
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:111
        self.getStatus = getStatus
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:112
        def _hx_local_5(fire):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:112
            _g = getStatus()
            if (_g.index == 1):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:113
                v = _g.params[0]
                fire(v)
                return None
            else:
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:115
                def _hx_local_4():
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:115
                    def _hx_local_3(s):
                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:115
                        if (s.index == 1):
                            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:117
                            v = s.params[0]
                            fire(v)
                    return changed.listen(_hx_local_3)
                return _hx_local_4()
        this1 = tink_core__Future_SuspendableFuture(_hx_local_5)
        self.result = this1

    def get_status(self):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:97
        return self.getStatus()

tink_core__Progress_ProgressObject._hx_class = tink_core__Progress_ProgressObject


class tink_core__Progress_SuspendableProgress(tink_core__Progress_ProgressObject):
    _hx_class_name = "tink.core._Progress.SuspendableProgress"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = ["noop"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = tink_core__Progress_ProgressObject


    def __init__(self,wakeup,status = None):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:75
        if (status is None):
            status = tink_core_ProgressStatus.InProgress(tink_core__Progress_ProgressValue_Impl_.ZERO)
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:77
        disposable = tink_core_AlreadyDisposed.INST
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:78
        changed = None
        changed1 = status.index
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:81
        if (changed1 == 0):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:81
            _g = status.params[0]
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:83
            def _hx_local_2(fire):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:83
                def _hx_local_1():
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:83
                    def _hx_local_0(s):
                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:83
                        nonlocal status
                        status = s
                        fire(status)
                    return wakeup(_hx_local_0)
                return _hx_local_1()
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:84
            def _hx_local_3(d):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:84
                nonlocal disposable
                disposable = d
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:82
            this1 = tink_core__Signal_Suspendable(_hx_local_2,_hx_local_3)
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:78
            changed = this1
        elif (changed1 == 1):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:79
            _g = status.params[0]
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:78
            changed = tink_core__Signal_Signal_Impl_.dead()
        else:
            pass
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:89
        def _hx_local_4():
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:89
            return status
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:87
        super().__init__(changed,_hx_local_4)

    def noop(self,_,_1):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:73
        return None

tink_core__Progress_SuspendableProgress._hx_class = tink_core__Progress_SuspendableProgress


class tink_core_ProgressTrigger(tink_core__Progress_ProgressObject):
    _hx_class_name = "tink.core.ProgressTrigger"
    _hx_is_interface = "False"
    __slots__ = ("_status", "_changed")
    _hx_fields = ["_status", "_changed"]
    _hx_methods = ["asProgress", "progress", "finish"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = tink_core__Progress_ProgressObject


    def __init__(self,status = None):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:125
        self._status = None
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:126
        self._changed = None
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:128
        _gthis = self
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:129
        if (status is None):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:130
            status = tink_core_ProgressStatus.InProgress(tink_core__Progress_ProgressValue_Impl_.ZERO)
            self._status = status
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:131
        tmp = None
        if (status is None):
            tmp = False
        elif (status.index == 1):
            _g = status.params[0]
            tmp = True
        else:
            tmp = False
        def _hx_local_2():
            def _hx_local_0():
                self._changed = tink_core__Signal_Signal_Impl_.trigger()
                return self._changed
            return tink_core__Signal_Signal_Impl_.dead() if tmp else _hx_local_0()
        def _hx_local_3():
            return _gthis._status
        super().__init__(_hx_local_2(),_hx_local_3)

    def asProgress(self):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:135
        return self

    def progress(self,v,total):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:138
        _g = self._status
        tmp = None
        if (_g.index == 1):
            _g1 = _g.params[0]
            tmp = True
        else:
            tmp = False
        if (not tmp):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:139
            _this = self._changed
            this1 = tink_core_MPair(v,total)
            this2 = this1
            def _hx_local_0():
                self._status = tink_core_ProgressStatus.InProgress(this2)
                return self._status
            _this.handlers.invoke(_hx_local_0())

    def finish(self,v):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:142
        _g = self._status
        tmp = None
        if (_g.index == 1):
            _g1 = _g.params[0]
            tmp = True
        else:
            tmp = False
        if (not tmp):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:143
            def _hx_local_0():
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:143
                self._status = tink_core_ProgressStatus.Finished(v)
                return self._status
            self._changed.handlers.invoke(_hx_local_0())

tink_core_ProgressTrigger._hx_class = tink_core_ProgressTrigger


class tink_core__Progress_UnitInterval_Impl_:
    _hx_class_name = "tink.core._Progress.UnitInterval_Impl_"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["toPercentageString"]

    @staticmethod
    def toPercentageString(this1,dp):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:172
        m = Math.pow(10,dp)
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:173
        v = (Math.floor((((this1 * m) * 100) + 0.5)) / m)
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:174
        s = Std.string(v)
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:175
        startIndex = None
        _g = (s.find(".") if ((startIndex is None)) else HxString.indexOfImpl(s,".",startIndex))
        if (_g == -1):
            return (((("null" if s is None else s) + ".") + HxOverrides.stringOrNull(StringTools.lpad("","0",dp))) + "%")
        else:
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:177
            i = _g
            if ((len(s) - i) > dp):
                return (HxOverrides.stringOrNull(HxString.substr(s,0,((dp + i) + 1))) + "%")
            else:
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:178
                i = _g
                return (HxOverrides.stringOrNull(StringTools.rpad(s,"0",((i + dp) + 1))) + "%")
tink_core__Progress_UnitInterval_Impl_._hx_class = tink_core__Progress_UnitInterval_Impl_

class tink_core_ProgressStatus(Enum):
    __slots__ = ()
    _hx_class_name = "tink.core.ProgressStatus"
    _hx_constructs = ["InProgress", "Finished"]

    @staticmethod
    def InProgress(v):
        return tink_core_ProgressStatus("InProgress", 0, (v,))

    @staticmethod
    def Finished(v):
        return tink_core_ProgressStatus("Finished", 1, (v,))
tink_core_ProgressStatus._hx_class = tink_core_ProgressStatus


class tink_core_ProgressStatusTools:
    _hx_class_name = "tink.core.ProgressStatusTools"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["map"]

    @staticmethod
    def map(p,f):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:199
        tmp = p.index
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:200
        if (tmp == 0):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:200
            v = p.params[0]
            return tink_core_ProgressStatus.InProgress(v)
        elif (tmp == 1):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:201
            v = p.params[0]
            return tink_core_ProgressStatus.Finished(f(v))
        else:
            pass
tink_core_ProgressStatusTools._hx_class = tink_core_ProgressStatusTools


class tink_core_TotalTools:
    _hx_class_name = "tink.core.TotalTools"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["eq"]

    @staticmethod
    def eq(a,b):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:208
        tmp = a.index
        if (tmp == 0):
            if (b.index == 0):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:209
                t2 = b.params[0]
                t1 = a.params[0]
                return (t1 == t2)
            else:
                return False
        elif (tmp == 1):
            if (b.index == 1):
                return True
            else:
                return False
        else:
            pass
tink_core_TotalTools._hx_class = tink_core_TotalTools


class tink_core_ProgressTools:
    _hx_class_name = "tink.core.ProgressTools"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["asPromise"]

    @staticmethod
    def asPromise(p):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:218
        return p.result
tink_core_ProgressTools._hx_class = tink_core_ProgressTools


class tink_core__Promise_Promise_Impl_:
    _hx_class_name = "tink.core._Promise.Promise_Impl_"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["NOISE", "NULL", "NEVER", "_new", "eager", "map", "flatMap", "tryRecover", "recover", "mapError", "handle", "noise", "isSuccess", "next", "swap", "swapError", "merge", "and", "iterate", "retry", "ofSpecific", "fromNever", "ofTrigger", "ofHappyTrigger", "ofFuture", "ofOutcome", "ofError", "ofData", "lazy", "inParallel", "many", "inSequence", "cache", "lift", "trigger", "resolve", "reject"]

    @staticmethod
    def _new(f):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:29
        def _hx_local_3(cb):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:29
            def _hx_local_2():
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:29
                def _hx_local_0(v):
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:29
                    cb(tink_core_Outcome.Success(v))
                def _hx_local_1(e):
                    cb(tink_core_Outcome.Failure(e))
                return f(_hx_local_0,_hx_local_1)
            return _hx_local_2()
        this1 = tink_core__Future_SuspendableFuture(_hx_local_3)
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:28
        this2 = this1
        return this2

    @staticmethod
    def eager(this1):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:32
        this1.eager()
        return this1

    @staticmethod
    def map(this1,f):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:35
        return tink_core__Future_Future_Impl_.map(this1,f)

    @staticmethod
    def flatMap(this1,f):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:38
        return tink_core__Future_Future_Impl_.flatMap(this1,f)

    @staticmethod
    def tryRecover(this1,f):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:41
        def _hx_local_1():
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:41
            def _hx_local_0(o):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:41
                tmp = o.index
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:42
                if (tmp == 0):
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:42
                    d = o.params[0]
                    return tink_core__Future_SyncFuture(tink_core__Lazy_LazyConst(o))
                elif (tmp == 1):
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:43
                    e = o.params[0]
                    return f(e)
                else:
                    pass
            return tink_core__Future_Future_Impl_.flatMap(this1,_hx_local_0)
        return _hx_local_1()

    @staticmethod
    def recover(this1,f):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:47
        def _hx_local_1():
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:47
            def _hx_local_0(o):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:47
                tmp = o.index
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:48
                if (tmp == 0):
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:48
                    d = o.params[0]
                    return tink_core__Future_SyncFuture(tink_core__Lazy_LazyConst(d))
                elif (tmp == 1):
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:49
                    e = o.params[0]
                    return f(e)
                else:
                    pass
            return tink_core__Future_Future_Impl_.flatMap(this1,_hx_local_0)
        return _hx_local_1()

    @staticmethod
    def mapError(this1,f):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:53
        def _hx_local_1():
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:53
            def _hx_local_0(o):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:53
                tmp = o.index
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:54
                if (tmp == 0):
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:54
                    _g = o.params[0]
                    return o
                elif (tmp == 1):
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:55
                    e = o.params[0]
                    return tink_core_Outcome.Failure(f(e))
                else:
                    pass
            return tink_core__Future_Future_Impl_.map(this1,_hx_local_0)
        return _hx_local_1()

    @staticmethod
    def handle(this1,cb):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:59
        return this1.handle(cb)

    @staticmethod
    def noise(this1):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:63
        if (this1.getStatus().index == 4):
            return tink_core__Promise_Promise_Impl_.NEVER
        else:
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:64
            def _hx_local_1():
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:64
                def _hx_local_0(v):
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:64
                    return tink_core__Future_SyncFuture(tink_core__Lazy_LazyConst(tink_core_Outcome.Success(None)))
                return tink_core__Promise_Promise_Impl_.next(this1,_hx_local_0)
            return _hx_local_1()

    @staticmethod
    def isSuccess(this1):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:67
        def _hx_local_1():
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:67
            def _hx_local_0(o):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:67
                return tink_core_OutcomeTools.isSuccess(o)
            return tink_core__Future_Future_Impl_.map(this1,_hx_local_0)
        return _hx_local_1()

    @staticmethod
    def next(this1,f,gather = None):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:70
        def _hx_local_1():
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:70
            def _hx_local_0(o):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:70
                tmp = o.index
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:71
                if (tmp == 0):
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:71
                    d = o.params[0]
                    return f(d)
                elif (tmp == 1):
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:72
                    f1 = o.params[0]
                    return tink_core__Future_SyncFuture(tink_core__Lazy_LazyConst(tink_core_Outcome.Failure(f1)))
                else:
                    pass
            return tink_core__Future_Future_Impl_.flatMap(this1,_hx_local_0)
        return _hx_local_1()

    @staticmethod
    def swap(this1,v):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:76
        def _hx_local_1():
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:76
            def _hx_local_0(_):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:76
                return tink_core__Future_SyncFuture(tink_core__Lazy_LazyConst(tink_core_Outcome.Success(v)))
            return tink_core__Promise_Promise_Impl_.next(this1,_hx_local_0)
        return _hx_local_1()

    @staticmethod
    def swapError(this1,e):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:79
        def _hx_local_1():
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:79
            def _hx_local_0(_):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:79
                return e
            return tink_core__Promise_Promise_Impl_.mapError(this1,_hx_local_0)
        return _hx_local_1()

    @staticmethod
    def merge(this1,other,merger,gather = None):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:82
        def _hx_local_2():
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:82
            def _hx_local_0(a,b):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:82
                tmp = a.index
                if (tmp == 0):
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:83
                    _g = a.params[0]
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:82
                    tmp = b.index
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:83
                    if (tmp == 0):
                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:83
                        b1 = b.params[0]
                        a1 = _g
                        return merger(a1,b1)
                    elif (tmp == 1):
                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:84
                        e = b.params[0]
                        return tink_core__Future_SyncFuture(tink_core__Lazy_LazyConst(tink_core_Outcome.Failure(e)))
                    else:
                        pass
                elif (tmp == 1):
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:84
                    e = a.params[0]
                    return tink_core__Future_SyncFuture(tink_core__Lazy_LazyConst(tink_core_Outcome.Failure(e)))
                else:
                    pass
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:85
            def _hx_local_1(o):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:85
                return o
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:82
            return tink_core__Future_Future_Impl_.flatMap(tink_core__Future_Future_Impl_.merge(this1,other,_hx_local_0),_hx_local_1)
        return _hx_local_2()

    @staticmethod
    def _hx_and(a,b):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:89
        def _hx_local_1():
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:89
            def _hx_local_0(a,b):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:89
                this1 = tink_core_MPair(a,b)
                return tink_core__Future_SyncFuture(tink_core__Lazy_LazyConst(tink_core_Outcome.Success(this1)))
            return tink_core__Promise_Promise_Impl_.merge(a,b,_hx_local_0)
        return _hx_local_1()

    @staticmethod
    def iterate(promises,_hx_yield,fallback):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:111
        def _hx_local_4():
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:111
            def _hx_local_3(cb):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:112
                _hx_iter = HxOverrides.iterator(promises)
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:113
                next = None
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:114
                def _hx_local_2():
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:114
                    if _hx_iter.hasNext():
                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:115
                        def _hx_local_1(o):
                            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:115
                            next1 = o.index
                            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:116
                            if (next1 == 0):
                                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:116
                                v = o.params[0]
                                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:117
                                def _hx_local_0(o):
                                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:117
                                    next1 = o.index
                                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:119
                                    if (next1 == 0):
                                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:119
                                        _g = o.params[0]
                                        next1 = _g.index
                                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:118
                                        if (next1 == 0):
                                            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:118
                                            ret = _g.params[0]
                                            cb(tink_core_Outcome.Success(ret))
                                        elif (next1 == 1):
                                            next()
                                        else:
                                            pass
                                    elif (next1 == 1):
                                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:120
                                        e = o.params[0]
                                        cb(tink_core_Outcome.Failure(e))
                                    else:
                                        pass
                                _hx_yield(v).handle(_hx_local_0)
                            elif (next1 == 1):
                                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:122
                                e = o.params[0]
                                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:123
                                cb(tink_core_Outcome.Failure(e))
                            else:
                                pass
                        _hx_iter.next().handle(_hx_local_1)
                    else:
                        fallback.handle(cb)
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:113
                next = _hx_local_2
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:128
                next()
            return tink_core__Future_Future_Impl_.irreversible(_hx_local_3)
        return _hx_local_4()

    @staticmethod
    def retry(gen,next):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:172
        def _hx_local_0():
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:172
            return (python_lib_Timeit.default_timer() * 1000)
        stamp = _hx_local_0
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:173
        start = stamp()
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:174
        attempt = None
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:175
        def _hx_local_6(count):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:177
            def _hx_local_3(error):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:177
                def _hx_local_2():
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:178
                    def _hx_local_1(_):
                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:178
                        return attempt((count + 1))
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:177
                    return tink_core__Promise_Promise_Impl_.next(next(_hx_AnonObject({'attempt': count, 'error': error, 'elapsed': (stamp() - start)})),_hx_local_1)
                return _hx_local_2()
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:175
            f = _hx_local_3
            def _hx_local_5():
                def _hx_local_4(o):
                    attempt = o.index
                    if (attempt == 0):
                        d = o.params[0]
                        return tink_core__Future_SyncFuture(tink_core__Lazy_LazyConst(o))
                    elif (attempt == 1):
                        e = o.params[0]
                        return f(e)
                    else:
                        pass
                return tink_core__Future_Future_Impl_.flatMap(gen(),_hx_local_4)
            return _hx_local_5()
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:174
        attempt = _hx_local_6
        return attempt(1)

    @staticmethod
    def ofSpecific(s):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:198
        return s

    @staticmethod
    def fromNever(l):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:201
        return l

    @staticmethod
    def ofTrigger(f):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:204
        return f

    @staticmethod
    def ofHappyTrigger(f):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:207
        return tink_core__Future_Future_Impl_.map(f,tink_core_Outcome.Success)

    @staticmethod
    def ofFuture(f):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:210
        return tink_core__Future_Future_Impl_.map(f,tink_core_Outcome.Success)

    @staticmethod
    def ofOutcome(o):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:213
        return tink_core__Future_SyncFuture(tink_core__Lazy_LazyConst(o))

    @staticmethod
    def ofError(e):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:216
        return tink_core__Future_SyncFuture(tink_core__Lazy_LazyConst(tink_core_Outcome.Failure(e)))

    @staticmethod
    def ofData(d):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:219
        return tink_core__Future_SyncFuture(tink_core__Lazy_LazyConst(tink_core_Outcome.Success(d)))

    @staticmethod
    def lazy(p):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:223
        def _hx_local_0(cb):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:223
            return tink_core__Lazy_Lazy_Impl_.get(p).handle(cb)
        this1 = tink_core__Future_SuspendableFuture(_hx_local_0)
        return this1

    @staticmethod
    def inParallel(a,concurrency = None):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:227
        return tink_core__Promise_Promise_Impl_.many(a,concurrency)

    @staticmethod
    def many(a,concurrency = None):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:230
        def _hx_local_2():
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:230
            def _hx_local_0(o):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:230
                return o
            def _hx_local_1(o):
                return o
            return tink_core__Future_Future_Impl_.processMany(a,concurrency,_hx_local_0,_hx_local_1)
        return _hx_local_2()

    @staticmethod
    def inSequence(a):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:234
        return tink_core__Promise_Promise_Impl_.many(a,1)

    @staticmethod
    def cache(gen):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:239
        p = None
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:240
        def _hx_local_0():
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:240
            nonlocal p
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:241
            ret = p
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:242
            if (ret is None):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:243
                sync = False
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:244
                def _hx_local_2(o):
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:245
                    def _hx_local_1(_):
                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:245
                        nonlocal p
                        nonlocal sync
                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:246
                        sync = True
                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:247
                        p = None
                    o.b.handle(_hx_local_1)
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:249
                    return tink_core__Future_SyncFuture(tink_core__Lazy_LazyConst(tink_core_Outcome.Success(o.a)))
                ret = tink_core__Promise_Promise_Impl_.next(gen(),_hx_local_2)
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:251
                if (not sync):
                    p = ret
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:253
            def _hx_local_4():
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:253
                def _hx_local_3(o):
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:253
                    nonlocal p
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:254
                    if (not tink_core_OutcomeTools.isSuccess(o)):
                        p = None
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:255
                    return o
                return tink_core__Future_Future_Impl_.map(ret,_hx_local_3)
            return _hx_local_4()
        return _hx_local_0

    @staticmethod
    def lift(p):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:263
        return p

    @staticmethod
    def trigger():
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:270
        this1 = tink_core_FutureTrigger()
        return this1

    @staticmethod
    def resolve(v):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:274
        return tink_core__Future_SyncFuture(tink_core__Lazy_LazyConst(tink_core_Outcome.Success(v)))

    @staticmethod
    def reject(e):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:278
        return tink_core__Future_SyncFuture(tink_core__Lazy_LazyConst(tink_core_Outcome.Failure(e)))
tink_core__Promise_Promise_Impl_._hx_class = tink_core__Promise_Promise_Impl_


class tink_core__Promise_Next_Impl_:
    _hx_class_name = "tink.core._Promise.Next_Impl_"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["ofSafe", "ofSync", "ofSafeSync", "_chain"]

    @staticmethod
    def ofSafe(f):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:291
        def _hx_local_0(x):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:291
            return tink_core__Future_SyncFuture(tink_core__Lazy_LazyConst(f(x)))
        return _hx_local_0

    @staticmethod
    def ofSync(f):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:294
        def _hx_local_0(x):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:294
            return tink_core__Future_Future_Impl_.map(f(x),tink_core_Outcome.Success)
        return _hx_local_0

    @staticmethod
    def ofSafeSync(f):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:297
        def _hx_local_0(x):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:297
            return tink_core__Future_SyncFuture(tink_core__Lazy_LazyConst(tink_core_Outcome.Success(f(x))))
        return _hx_local_0

    @staticmethod
    def _chain(a,b):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:300
        def _hx_local_0(v):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:300
            return tink_core__Promise_Promise_Impl_.next(a(v),b)
        return _hx_local_0
tink_core__Promise_Next_Impl_._hx_class = tink_core__Promise_Next_Impl_


class tink_core__Promise_Recover_Impl_:
    _hx_class_name = "tink.core._Promise.Recover_Impl_"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["ofSync"]

    @staticmethod
    def ofSync(f):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:309
        def _hx_local_0(e):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:309
            return tink_core__Future_SyncFuture(tink_core__Lazy_LazyConst(f(e)))
        return _hx_local_0
tink_core__Promise_Recover_Impl_._hx_class = tink_core__Promise_Recover_Impl_


class tink_core__Promise_Combiner_Impl_:
    _hx_class_name = "tink.core._Promise.Combiner_Impl_"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["ofSync", "ofSafe", "ofSafeSync"]

    @staticmethod
    def ofSync(f):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:316
        def _hx_local_0(x1,x2):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:316
            return tink_core__Future_SyncFuture(tink_core__Lazy_LazyConst(f(x1,x2)))
        return _hx_local_0

    @staticmethod
    def ofSafe(f):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:319
        def _hx_local_0(x1,x2):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:319
            return tink_core__Future_Future_Impl_.map(f(x1,x2),tink_core_Outcome.Success)
        return _hx_local_0

    @staticmethod
    def ofSafeSync(f):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:322
        def _hx_local_0(x1,x2):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:322
            return tink_core__Future_SyncFuture(tink_core__Lazy_LazyConst(tink_core_Outcome.Success(f(x1,x2))))
        return _hx_local_0
tink_core__Promise_Combiner_Impl_._hx_class = tink_core__Promise_Combiner_Impl_


class tink_core__Promise_PromiseTrigger_Impl_:
    _hx_class_name = "tink.core._Promise.PromiseTrigger_Impl_"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["_new", "resolve", "reject", "asPromise"]

    @staticmethod
    def _new():
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:329
        this1 = tink_core_FutureTrigger()
        return this1

    @staticmethod
    def resolve(this1,v):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:333
        return this1.trigger(tink_core_Outcome.Success(v))

    @staticmethod
    def reject(this1,e):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:336
        return this1.trigger(tink_core_Outcome.Failure(e))

    @staticmethod
    def asPromise(this1):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Promise.hx:338
        return this1
tink_core__Promise_PromiseTrigger_Impl_._hx_class = tink_core__Promise_PromiseTrigger_Impl_


class tink_core__Ref_Ref_Impl_:
    _hx_class_name = "tink.core._Ref.Ref_Impl_"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["_new", "get_value", "set_value", "toString", "to"]
    value = None

    @staticmethod
    def _new():
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Ref.hx:6
        this1 = [None]*1
        this2 = this1
        return this2

    @staticmethod
    def get_value(this1):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Ref.hx:8
        return this1[0]

    @staticmethod
    def set_value(this1,param):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Ref.hx:9
        this1[0] = param
        return param

    @staticmethod
    def toString(this1):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Ref.hx:11
        return (("@[" + Std.string(this1[0])) + "]")

    @staticmethod
    def to(v):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Ref.hx:14
        this1 = [None]*1
        this2 = this1
        ret = this2
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Ref.hx:15
        ret[0] = v
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Ref.hx:16
        return ret
tink_core__Ref_Ref_Impl_._hx_class = tink_core__Ref_Ref_Impl_


class tink_core__Signal_Gather_Impl_:
    _hx_class_name = "tink.core._Signal.Gather_Impl_"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["_new", "ofBool"]

    @staticmethod
    def _new(v):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:9
        this1 = v
        return this1

    @staticmethod
    def ofBool(b):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:12
        this1 = b
        return this1
tink_core__Signal_Gather_Impl_._hx_class = tink_core__Signal_Gather_Impl_


class tink_core__Signal_Signal_Impl_:
    _hx_class_name = "tink.core._Signal.Signal_Impl_"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_statics = ["_new", "handle", "map", "flatMap", "filter", "select", "join", "nextTime", "pickNext", "until", "next", "noise", "gather", "create", "generate", "trigger", "ofClassical", "dead"]

    @staticmethod
    def _new(f,init = None):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:22
        this1 = tink_core__Signal_Suspendable(f,init)
        return this1

    @staticmethod
    def handle(this1,handler):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:26
        return this1.listen(handler)

    @staticmethod
    def map(this1,f,gather = None):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:33
        def _hx_local_3():
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:33
            def _hx_local_2(fire):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:33
                def _hx_local_1():
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:33
                    def _hx_local_0(v):
                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:33
                        fire(f(v))
                    return this1.listen(_hx_local_0)
                return _hx_local_1()
            return tink_core__Signal_Suspendable.over(this1,_hx_local_2)
        return _hx_local_3()

    @staticmethod
    def flatMap(this1,f,gather = None):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:40
        def _hx_local_3():
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:40
            def _hx_local_2(fire):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:40
                def _hx_local_1():
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:40
                    def _hx_local_0(v):
                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:40
                        f(v).handle(fire)
                    return this1.listen(_hx_local_0)
                return _hx_local_1()
            return tink_core__Signal_Suspendable.over(this1,_hx_local_2)
        return _hx_local_3()

    @staticmethod
    def filter(this1,f,gather = None):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:46
        def _hx_local_3():
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:46
            def _hx_local_2(fire):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:46
                def _hx_local_1():
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:46
                    def _hx_local_0(v):
                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:46
                        if f(v):
                            fire(v)
                    return this1.listen(_hx_local_0)
                return _hx_local_1()
            return tink_core__Signal_Suspendable.over(this1,_hx_local_2)
        return _hx_local_3()

    @staticmethod
    def select(this1,selector,gather = None):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:49
        def _hx_local_3():
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:49
            def _hx_local_2(fire):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:49
                def _hx_local_1():
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:49
                    def _hx_local_0(v):
                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:49
                        _g = selector(v)
                        if (_g.index == 0):
                            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:50
                            v = _g.params[0]
                            fire(v)
                    return this1.listen(_hx_local_0)
                return _hx_local_1()
            return tink_core__Signal_Suspendable.over(this1,_hx_local_2)
        return _hx_local_3()

    @staticmethod
    def join(this1,that,gather = None):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:60
        if this1.get_disposed():
            return that
        elif that.get_disposed():
            return this1
        else:
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:62
            def _hx_local_3():
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:63
                def _hx_local_0(fire):
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:64
                    cb = fire
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:65
                    return tink_core__Callback_LinkPair(this1.listen(cb),that.listen(cb))
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:67
                def _hx_local_2(_hx_self):
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:69
                    def _hx_local_1():
                        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:69
                        if (this1.get_disposed() and that.get_disposed()):
                            _hx_self.dispose()
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:68
                    release = _hx_local_1
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:70
                    this1.ondispose(release)
                    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:71
                    that.ondispose(release)
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:62
                return tink_core__Signal_Suspendable(_hx_local_0,_hx_local_2)
            return _hx_local_3()

    @staticmethod
    def nextTime(this1,condition = None):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:79
        def _hx_local_1():
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:79
            def _hx_local_0(v):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:79
                if ((condition is None) or condition(v)):
                    return haxe_ds_Option.Some(v)
                else:
                    return haxe_ds_Option._hx_None
            return tink_core__Signal_Signal_Impl_.pickNext(this1,_hx_local_0)
        return _hx_local_1()

    @staticmethod
    def pickNext(this1,selector):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:85
        ret = tink_core_FutureTrigger()
        link = None
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:88
        def _hx_local_0(v):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:88
            _g = selector(v)
            link = _g.index
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:90
            if (link == 0):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:90
                v = _g.params[0]
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:91
                ret.trigger(v)
            elif (link == 1):
                pass
            else:
                pass
        link = this1.listen(_hx_local_0)
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:94
        tmp = None
        if (link is None):
            def _hx_local_1(_):
                tink_core__Callback_CallbackLink_Impl_.noop()
            tmp = _hx_local_1
        else:
            f = link.cancel
            def _hx_local_2(_):
                f()
            tmp = _hx_local_2
        ret.handle(tmp)
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:96
        return ret

    @staticmethod
    def until(this1,end):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:100
        def _hx_local_3():
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:101
            def _hx_local_0(_hx_yield):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:101
                return this1.listen(_hx_yield)
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:102
            def _hx_local_2(_hx_self):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:102
                f = _hx_self.dispose
                def _hx_local_1(_):
                    f()
                tmp = _hx_local_1
                end.handle(tmp)
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:100
            return tink_core__Signal_Suspendable(_hx_local_0,_hx_local_2)
        return _hx_local_3()

    @staticmethod
    def next(this1,condition = None):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:107
        return tink_core__Signal_Signal_Impl_.nextTime(this1,condition)

    @staticmethod
    def noise(this1):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:113
        def _hx_local_1():
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:113
            def _hx_local_0(_):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:113
                return None
            return tink_core__Signal_Signal_Impl_.map(this1,_hx_local_0)
        return _hx_local_1()

    @staticmethod
    def gather(this1):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:122
        return this1

    @staticmethod
    def create(f):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:126
        this1 = tink_core__Signal_Suspendable(f,None)
        return this1

    @staticmethod
    def generate(generator,init = None):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:133
        def _hx_local_0(fire):
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:133
            generator(fire)
            return None
        this1 = tink_core__Signal_Suspendable(_hx_local_0,init)
        return this1

    @staticmethod
    def trigger():
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:139
        return tink_core_SignalTrigger()

    @staticmethod
    def ofClassical(add,remove,gather = None):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:146
        def _hx_local_2():
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:146
            def _hx_local_1(fire):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:147
                add(fire)
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:148
                _g = remove
                a1 = fire
                def _hx_local_0():
                    _g(a1)
                this1 = tink_core_SimpleLink(_hx_local_0)
                return this1
            return tink_core__Signal_Suspendable(_hx_local_1)
        return _hx_local_2()

    @staticmethod
    def dead():
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:152
        return tink_core__Signal_Disposed.INST
tink_core__Signal_Signal_Impl_._hx_class = tink_core__Signal_Signal_Impl_


class tink_core__Signal_SignalObject:
    _hx_class_name = "tink.core._Signal.SignalObject"
    _hx_is_interface = "True"
    __slots__ = ()
    _hx_methods = ["listen"]
    _hx_interfaces = [tink_core_Disposable]
tink_core__Signal_SignalObject._hx_class = tink_core__Signal_SignalObject


class tink_core__Signal_Disposed(tink_core_AlreadyDisposed):
    _hx_class_name = "tink.core._Signal.Disposed"
    _hx_is_interface = "False"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = ["listen"]
    _hx_statics = ["INST"]
    _hx_interfaces = [tink_core__Signal_SignalObject]
    _hx_super = tink_core_AlreadyDisposed


    def __init__(self):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:155
        super().__init__()

    def listen(self,cb):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:160
        return None

tink_core__Signal_Disposed._hx_class = tink_core__Signal_Disposed


class tink_core__Signal_Suspendable:
    _hx_class_name = "tink.core._Signal.Suspendable"
    _hx_is_interface = "False"
    __slots__ = ("handlers", "activate", "init", "subscription")
    _hx_fields = ["handlers", "activate", "init", "subscription"]
    _hx_methods = ["get_disposed", "dispose", "ondispose", "listen"]
    _hx_statics = ["over"]
    _hx_interfaces = [tink_core_OwnedDisposable, tink_core__Signal_SignalObject]

    def __init__(self,activate,init = None):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:169
        self.subscription = None
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:168
        self.init = None
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:166
        self.activate = None
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:165
        self.handlers = tink_core_CallbackList()
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:180
        _gthis = self
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:181
        self.activate = activate
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:182
        self.init = init
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:184
        def _hx_local_0():
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:184
            this1 = _gthis.subscription
            if (this1 is not None):
                this1.cancel()
        self.handlers.ondrain = _hx_local_0
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:185
        def _hx_local_1():
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:185
            nonlocal init
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:186
            if (init is not None):
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:188
                f = init
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:189
                init = None
                # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:190
                f(_gthis)
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:192
            _gthis.subscription = activate(_gthis.handlers.invoke)
        self.handlers.onfill = _hx_local_1

    def get_disposed(self):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:172
        return (self.handlers.disposeHandlers is None)

    def dispose(self):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:175
        self.handlers.dispose()

    def ondispose(self,handler):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:178
        self.handlers.ondispose(handler)

    def listen(self,cb):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:197
        _this = self.handlers
        if (_this.disposeHandlers is None):
            return None
        else:
            node = tink_core__Callback_ListCell(cb,_this)
            _this1 = _this.cells
            _this1.append(node)
            def _hx_local_1():
                _hx_local_0 = _this.used
                _this.used = (_this.used + 1)
                return _hx_local_0
            tmp = (_hx_local_1() == 0)
            if tmp:
                fn = _this.onfill
                if (tink_core__Callback_Callback_Impl_.depth < 100):
                    _hx_local_2 = tink_core__Callback_Callback_Impl_
                    _hx_local_3 = _hx_local_2.depth
                    _hx_local_2.depth = (_hx_local_3 + 1)
                    _hx_local_3
                    fn()
                    _hx_local_4 = tink_core__Callback_Callback_Impl_
                    _hx_local_5 = _hx_local_4.depth
                    _hx_local_4.depth = (_hx_local_5 - 1)
                    _hx_local_5
                else:
                    tink_core__Callback_Callback_Impl_.defer(fn)
            return node

    @staticmethod
    def over(s,activate):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:201
        if s.get_disposed():
            return tink_core__Signal_Signal_Impl_.dead()
        else:
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:203
            ret = tink_core__Signal_Suspendable(activate)
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:204
            s.ondispose(ret.dispose)
            # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:205
            return ret

tink_core__Signal_Suspendable._hx_class = tink_core__Signal_Suspendable


class tink_core_SignalTrigger:
    _hx_class_name = "tink.core.SignalTrigger"
    _hx_is_interface = "False"
    __slots__ = ("handlers",)
    _hx_fields = ["handlers"]
    _hx_methods = ["get_disposed", "dispose", "ondispose", "trigger", "getLength", "listen", "clear", "asSignal"]
    _hx_interfaces = [tink_core_OwnedDisposable, tink_core__Signal_SignalObject]

    def __init__(self):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:214
        self.handlers = tink_core_CallbackList()

    def get_disposed(self):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:212
        return (self.handlers.disposeHandlers is None)

    def dispose(self):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:219
        self.handlers.dispose()

    def ondispose(self,d):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:222
        self.handlers.ondispose(d)

    def trigger(self,event):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:228
        self.handlers.invoke(event)

    def getLength(self):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:234
        return self.handlers.used

    def listen(self,cb):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:237
        _this = self.handlers
        if (_this.disposeHandlers is None):
            return None
        else:
            node = tink_core__Callback_ListCell(cb,_this)
            _this1 = _this.cells
            _this1.append(node)
            def _hx_local_1():
                _hx_local_0 = _this.used
                _this.used = (_this.used + 1)
                return _hx_local_0
            tmp = (_hx_local_1() == 0)
            if tmp:
                fn = _this.onfill
                if (tink_core__Callback_Callback_Impl_.depth < 100):
                    _hx_local_2 = tink_core__Callback_Callback_Impl_
                    _hx_local_3 = _hx_local_2.depth
                    _hx_local_2.depth = (_hx_local_3 + 1)
                    _hx_local_3
                    fn()
                    _hx_local_4 = tink_core__Callback_Callback_Impl_
                    _hx_local_5 = _hx_local_4.depth
                    _hx_local_4.depth = (_hx_local_5 - 1)
                    _hx_local_5
                else:
                    tink_core__Callback_Callback_Impl_.defer(fn)
            return node

    def clear(self):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:243
        self.handlers.clear()

    def asSignal(self):
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Signal.hx:246
        return self

tink_core_SignalTrigger._hx_class = tink_core_SignalTrigger

# /Users/glen/bin/haxe-4.2.5/std/python/_std/Math.hx:126
Math.NEGATIVE_INFINITY = float("-inf")
# /Users/glen/bin/haxe-4.2.5/std/python/_std/Math.hx:127
Math.POSITIVE_INFINITY = float("inf")
# /Users/glen/bin/haxe-4.2.5/std/python/_std/Math.hx:128
Math.NaN = float("nan")
# /Users/glen/bin/haxe-4.2.5/std/python/_std/Math.hx:129
Math.PI = python_lib_Math.pi
# /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/thread/Thread.hx:79
sys_thread__Thread_HxThread.threads = haxe_ds_ObjectMap()
# /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/thread/Thread.hx:80
sys_thread__Thread_HxThread.threadsMutex = sys_thread_Mutex()
# /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/thread/Thread.hx:81
sys_thread__Thread_HxThread.mainThread = sys_thread__Thread_HxThread(threading.current_thread())
# /Users/glen/bin/haxe-4.2.5/std/python/_std/sys/thread/Thread.hx:82
sys_thread__Thread_HxThread.mainThread.events = sys_thread_EventLoop()

Sys._programPath = sys_FileSystem.fullPath(python_lib_Inspect.getsourcefile(Sys))
a8_Constants.a8VersionsVersion = "1.0.0-20221106_1642_master"
python_Lib.lineEnd = ("\r\n" if ((Sys.systemName() == "Windows")) else "\n")
def _hx_init_a8_GlobalScheduler_scheduler():
    # src/a8/GlobalScheduler.hx:9
    def _hx_local_0():
        # src/a8/GlobalScheduler.hx:10
        s = a8_PySched.scheduler()
        # src/a8/GlobalScheduler.hx:12
        def _hx_local_1():
            # src/a8/GlobalScheduler.hx:12
            while True:
                # src/a8/GlobalScheduler.hx:13
                s.run()
                # src/a8/GlobalScheduler.hx:14
                python_lib_Time.sleep(1)
        # src/a8/GlobalScheduler.hx:11
        a8_PyOps.spawn(_hx_local_1)
        # src/a8/GlobalScheduler.hx:17
        return s
    return _hx_local_0()
a8_GlobalScheduler.scheduler = _hx_init_a8_GlobalScheduler_scheduler()
a8_Logger.traceEnabled = False
a8_PlatformOps.instance = a8_PythonPlatform()
a8_UserConfig.repoConfig = a8_PathOps.readProperties(a8_PathOps.entry(a8_PathOps.userHome(),".a8/repo.properties"))
python_Boot.keywords = set(["and", "del", "from", "not", "with", "as", "elif", "global", "or", "yield", "assert", "else", "if", "pass", "None", "break", "except", "import", "raise", "True", "class", "exec", "in", "return", "False", "continue", "finally", "is", "try", "def", "for", "lambda", "while"])
python_Boot.prefixLength = len("_hx_")
sys_Http.PROXY = None
tink_core__Callback_Callback_Impl_.depth = 0
tink_core__Callback_Callback_Impl_.MAX_DEPTH = 100
tink_core_AlreadyDisposed.INST = tink_core_AlreadyDisposed()
tink_core__Future_Future_Impl_.NOISE = tink_core__Future_SyncFuture(tink_core__Lazy_LazyConst(None))
tink_core__Future_Future_Impl_.NULL = tink_core__Future_Future_Impl_.NOISE
tink_core__Future_Future_Impl_.NEVER = tink_core__Future_NeverFuture()
tink_core__Lazy_Lazy_Impl_.NOISE = tink_core__Lazy_LazyConst(None)
tink_core__Lazy_Lazy_Impl_.NULL = tink_core__Lazy_Lazy_Impl_.NOISE
tink_core__Noise_Noise_Impl_.Noise = None
def _hx_init_tink_core__Progress_ProgressValue_Impl__ZERO():
    # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:149
    def _hx_local_0():
        # /usr/local/lib/haxe/lib/tink_core/2,0,2/src/tink/core/Progress.hx:149
        this1 = tink_core_MPair(0,haxe_ds_Option._hx_None)
        this2 = this1
        return this2
    return _hx_local_0()
tink_core__Progress_ProgressValue_Impl_.ZERO = _hx_init_tink_core__Progress_ProgressValue_Impl__ZERO()
tink_core__Progress_Progress_Impl_.INIT = tink_core__Progress_ProgressValue_Impl_.ZERO
tink_core__Promise_Promise_Impl_.NOISE = tink_core__Future_SyncFuture(tink_core__Lazy_LazyConst(tink_core_Outcome.Success(None)))
tink_core__Promise_Promise_Impl_.NULL = tink_core__Promise_Promise_Impl_.NOISE
tink_core__Promise_Promise_Impl_.NEVER = tink_core__Future_Future_Impl_.NEVER
tink_core__Signal_Disposed.INST = tink_core__Signal_Disposed()

a8_launcher_Main.main()
sys_thread__Thread_Thread_Impl_.processEvents()
