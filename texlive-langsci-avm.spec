Name:		texlive-langsci-avm
Version:	66016
Release:	1
Summary:	Attribute-value matrices and feature structures for use in linguistics
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/langsci-avm
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/langsci-avm.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/langsci-avm.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/langsci-avm.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is aimed at typesetting beautiful feature
structures, also known as attribute-value matrices (AVMs), for
use in linguistics. The package provides a minimal and easy to
read syntax. It depends only on the array package and can be
placed almost everywhere, in particular in footnotes or graphs
and tree structures. The package is meant as an update to, and
serves the same purpose as, Christopher Manning's avm package,
but shares no code base with that package. langsci-avm was
developed at Language Science Press to help in the production
of scientific texts in linguistics, in particular an upcoming
HPSG handbook.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/langsci-avm
%{_texmfdistdir}/tex/latex/langsci-avm
%doc %{_texmfdistdir}/doc/latex/langsci-avm

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
