Name:		texlive-ltxguidex
Version:	50992
Release:	1
Summary:	An extended ltxguide class
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ltxguidex
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ltxguidex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ltxguidex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The ltxguidex document class extends ltxguide with a set of
environments and commands that make writing beautiful LaTeX
documentation easier and more natural.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/ltxguidex
%doc %{_texmfdistdir}/doc/latex/ltxguidex

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
