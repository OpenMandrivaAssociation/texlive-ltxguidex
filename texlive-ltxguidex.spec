%global tl_name ltxguidex
%global tl_revision 50992

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2.0
Release:	%{tl_revision}.1
Summary:	An extended ltxguide class
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ltxguidex
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ltxguidex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ltxguidex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The ltxguidex document class extends ltxguide with a set of environments
and commands that make writing beautiful LaTeX documentation easier and
more natural.

