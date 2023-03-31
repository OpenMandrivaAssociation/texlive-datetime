Name:		texlive-datetime
Version:	36650
Release:	2
Summary:	Change format of \today with commands for current time
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/datetime
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/datetime.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/datetime.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/datetime.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
