Name:		texlive-cooking
Version:	15878
Release:	1
Summary:	Typeset recipes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cooking
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cooking.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cooking.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cooking.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package typesets recipes according to the style used in a
well-respected German cookery book.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/cooking/cooking.sty
%doc %{_texmfdistdir}/doc/latex/cooking/COPYING
%doc %{_texmfdistdir}/doc/latex/cooking/README
%doc %{_texmfdistdir}/doc/latex/cooking/cooking.pdf
%doc %{_texmfdistdir}/doc/latex/cooking/kraut.tex
#- source
%doc %{_texmfdistdir}/source/latex/cooking/cooking.dtx
%doc %{_texmfdistdir}/source/latex/cooking/cooking.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
