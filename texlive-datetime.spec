Name:		texlive-datetime
Version:	2.60
Release:	1
Summary:	Change format of \today with commands for current time
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/datetime
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/datetime.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/datetime.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/datetime.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-fmtcount

%description
Provides various different formats for the text created by the
command \today, and also provides commands for displaying the
current time (or any given time), in 12-hour, 24-hour or text
format. The package overrides babel's date format, having its
own library of date formats in different languages. The package
requires the fmtcount package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/datetime
%doc %{_texmfdistdir}/doc/latex/datetime
#- source
%doc %{_texmfdistdir}/source/latex/datetime

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
