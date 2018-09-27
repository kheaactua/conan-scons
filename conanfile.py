#!/usr/bin/env python
# -*- coding: future_fstrings -*-
# -*- coding: utf-8 -*-

import os, shutil, sys, platform
from conans import ConanFile, tools
from glob import glob


class SconsConan(ConanFile):
    name        = 'scons'
    version     = '3.0.1'
    license     = 'MIT'
    url         = 'https://github.com/kheaactua/conan-scons'
    description = 'Use SCons 3'
    md5_hash    = 'b6a292e251b34b82c203b56cfa3968b3'
    requires    = 'helpers/[>=0.3]@ntc/stable'

    settings = {
        'os_build':   ['Windows', 'Linux', 'Macos'],
        'arch_build': ['x86', 'x86_64', 'armv7'],
    }

    def source(self):
        archive = 'scons-%s'%self.version
        archive_file = '%s.tar.gz'%archive
        url = 'http://prdownloads.sourceforge.net/scons/%s'%archive_file

        from source_cache import copyFromCache
        if not copyFromCache(archive_file):
            tools.download(url=url, filename=archive_file)
            tools.check_md5(archive_file, self.md5_hash)
        tools.unzip(archive_file)
        shutil.move(archive, self.name)
        os.remove(archive_file)

    def build(self):
        with tools.chdir(self.name):
            self.run(f'python setup.py install --prefix={self.package_folder}')

    def package_info(self):
        self.env_info.path.append(os.path.join(self.package_folder, 'bin'))

# vim: ts=4 sw=4 expandtab ffs=unix ft=python foldmethod=marker :
