#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-startupmsg
Version  : 0.9.5
Release  : 1
URL      : https://cran.r-project.org/src/contrib/startupmsg_0.9.5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/startupmsg_0.9.5.tar.gz
Summary  : Utilities for Start-Up Messages
Group    : Development/Tools
License  : LGPL-3.0
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n startupmsg

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1550859992

%install
export SOURCE_DATE_EPOCH=1550859992
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library startupmsg
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library startupmsg
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library startupmsg
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library startupmsg|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/startupmsg/DESCRIPTION
/usr/lib64/R/library/startupmsg/INDEX
/usr/lib64/R/library/startupmsg/Meta/Rd.rds
/usr/lib64/R/library/startupmsg/Meta/features.rds
/usr/lib64/R/library/startupmsg/Meta/hsearch.rds
/usr/lib64/R/library/startupmsg/Meta/links.rds
/usr/lib64/R/library/startupmsg/Meta/nsInfo.rds
/usr/lib64/R/library/startupmsg/Meta/package.rds
/usr/lib64/R/library/startupmsg/NAMESPACE
/usr/lib64/R/library/startupmsg/NEWS
/usr/lib64/R/library/startupmsg/R/startupmsg
/usr/lib64/R/library/startupmsg/R/startupmsg.rdb
/usr/lib64/R/library/startupmsg/R/startupmsg.rdx
/usr/lib64/R/library/startupmsg/TOBEDONE
/usr/lib64/R/library/startupmsg/help/AnIndex
/usr/lib64/R/library/startupmsg/help/aliases.rds
/usr/lib64/R/library/startupmsg/help/paths.rds
/usr/lib64/R/library/startupmsg/help/startupmsg.rdb
/usr/lib64/R/library/startupmsg/help/startupmsg.rdx
/usr/lib64/R/library/startupmsg/html/00Index.html
/usr/lib64/R/library/startupmsg/html/R.css