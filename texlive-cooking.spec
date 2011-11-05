# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/cooking
# catalog-date 2006-12-09 15:50:57 +0100
# catalog-license gpl
# catalog-version 0.9b
Name:		texlive-cooking
Version:	0.9b
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package typesets recipes according to the style used in a
well-respected German cookery book.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
