Name:		texlive-datetime
Version:	2.58
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
Requires(post):	texlive-tlpkg
Requires:	texlive-fmtcount
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Provides various different formats for the text created by the
command \today, and also provides commands for displaying the
current time (or any given time), in 12-hour, 24-hour or text
format. The package overrides babel's date format, having its
own library of date formats in different languages. The package
requires the fmtcount package.

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
%{_texmfdistdir}/tex/latex/datetime/datetime.sty
%{_texmfdistdir}/tex/latex/datetime/dt-UKenglish.def
%{_texmfdistdir}/tex/latex/datetime/dt-USenglish.def
%{_texmfdistdir}/tex/latex/datetime/dt-american.def
%{_texmfdistdir}/tex/latex/datetime/dt-austrian.def
%{_texmfdistdir}/tex/latex/datetime/dt-bahasa.def
%{_texmfdistdir}/tex/latex/datetime/dt-basque.def
%{_texmfdistdir}/tex/latex/datetime/dt-breton.def
%{_texmfdistdir}/tex/latex/datetime/dt-british.def
%{_texmfdistdir}/tex/latex/datetime/dt-bulgarian.def
%{_texmfdistdir}/tex/latex/datetime/dt-catalan.def
%{_texmfdistdir}/tex/latex/datetime/dt-croatian.def
%{_texmfdistdir}/tex/latex/datetime/dt-czech.def
%{_texmfdistdir}/tex/latex/datetime/dt-danish.def
%{_texmfdistdir}/tex/latex/datetime/dt-dutch.def
%{_texmfdistdir}/tex/latex/datetime/dt-esperanto.def
%{_texmfdistdir}/tex/latex/datetime/dt-estonian.def
%{_texmfdistdir}/tex/latex/datetime/dt-finnish.def
%{_texmfdistdir}/tex/latex/datetime/dt-french.def
%{_texmfdistdir}/tex/latex/datetime/dt-galician.def
%{_texmfdistdir}/tex/latex/datetime/dt-german.def
%{_texmfdistdir}/tex/latex/datetime/dt-greek.def
%{_texmfdistdir}/tex/latex/datetime/dt-hebrew.def
%{_texmfdistdir}/tex/latex/datetime/dt-icelandic.def
%{_texmfdistdir}/tex/latex/datetime/dt-irish.def
%{_texmfdistdir}/tex/latex/datetime/dt-italian.def
%{_texmfdistdir}/tex/latex/datetime/dt-latin.def
%{_texmfdistdir}/tex/latex/datetime/dt-lsorbian.def
%{_texmfdistdir}/tex/latex/datetime/dt-magyar.def
%{_texmfdistdir}/tex/latex/datetime/dt-naustrian.def
%{_texmfdistdir}/tex/latex/datetime/dt-ngerman.def
%{_texmfdistdir}/tex/latex/datetime/dt-norsk.def
%{_texmfdistdir}/tex/latex/datetime/dt-polish.def
%{_texmfdistdir}/tex/latex/datetime/dt-portuges.def
%{_texmfdistdir}/tex/latex/datetime/dt-romanian.def
%{_texmfdistdir}/tex/latex/datetime/dt-russian.def
%{_texmfdistdir}/tex/latex/datetime/dt-samin.def
%{_texmfdistdir}/tex/latex/datetime/dt-scottish.def
%{_texmfdistdir}/tex/latex/datetime/dt-serbian.def
%{_texmfdistdir}/tex/latex/datetime/dt-slovak.def
%{_texmfdistdir}/tex/latex/datetime/dt-slovene.def
%{_texmfdistdir}/tex/latex/datetime/dt-spanish.def
%{_texmfdistdir}/tex/latex/datetime/dt-swedish.def
%{_texmfdistdir}/tex/latex/datetime/dt-turkish.def
%{_texmfdistdir}/tex/latex/datetime/dt-ukraineb.def
%{_texmfdistdir}/tex/latex/datetime/dt-usorbian.def
%{_texmfdistdir}/tex/latex/datetime/dt-welsh.def
%doc %{_texmfdistdir}/doc/latex/datetime/CHANGES
%doc %{_texmfdistdir}/doc/latex/datetime/README
%doc %{_texmfdistdir}/doc/latex/datetime/datetime-manual.css
%doc %{_texmfdistdir}/doc/latex/datetime/datetime-manual.html
%doc %{_texmfdistdir}/doc/latex/datetime/datetime-manual.tex
%doc %{_texmfdistdir}/doc/latex/datetime/datetime.pdf
#- source
%doc %{_texmfdistdir}/source/latex/datetime/datetime.dtx
%doc %{_texmfdistdir}/source/latex/datetime/datetime.ins
%doc %{_texmfdistdir}/source/latex/datetime/datetime.perl

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}