Format: 3.0 (quilt)
Source: leveldb
Binary: libleveldb1v5, libleveldb-dev, libleveldb-dbg, leveldb-doc
Architecture: any all
Version: 2.0.17
Maintainer: Matthew Heller <matthew.f.heller@accre.vanderbilt.edu>
Homepage: https://github.com/basho/leveldb
Standards-Version: 3.9.6
Vcs-Browser: https://github.com/accre/leveldb
Vcs-Git: git://github.com/accre/leveldb
Build-Depends: debhelper (>= 9), libsnappy-dev (>= 1.0)
Package-List: 
 leveldb-doc deb doc optional
 libleveldb-dbg deb debug extra
 libleveldb-dev deb libdevel optional
 libleveldb1v5 deb libs optional
Checksums-Sha1: 
 c18bc601b37fe00570738582f3e79215111e5a2c 324325 leveldb_2.0.17.orig.tar.gz
 6a4d7f63edb72e0d35144b8c80e1cca833e2485a 7437 leveldb_2.0.17.debian.tar.gz
Checksums-Sha256: 
 ef108d7dd20b9f23a7dd9264e09711d51743d25a77b74970aa6d50d14f162bcf 324325 leveldb_2.0.17.orig.tar.gz
 413375bc23811abd4040045a1521ab30a7a92af1689e0a81a1082327583eb83e 7437 leveldb_2.0.17.debian.tar.gz
Files: 
 ce67db25313e49baccbd23c7943923c4 324325 leveldb_2.0.17.orig.tar.gz
 5060d062d59a7c4fd2b4e146b31fc80e 7437 leveldb_2.0.17.debian.tar.gz
Testsuite: autopkgtest
