# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/cooking
# catalog-date 2006-12-09 15:50:57 +0100
# catalog-license gpl
# catalog-version 0.9b
Name:		texlive-cooking
Version:	0.9b
Release:	10
Summary:	Typeset recipes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cooking
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cooking.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cooking.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cooking.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.9b-2
+ Revision: 750546
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.9b-1
+ Revision: 718148
- texlive-cooking
- texlive-cooking
- texlive-cooking
- texlive-cooking

