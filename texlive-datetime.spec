%global tl_name datetime
%global tl_revision 36650

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.60
Release:	%{tl_revision}.1
Summary:	Change format of \today with commands for current time
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/obsolete/macros/latex/contrib/datetime
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/datetime.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/datetime.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/datetime.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Provides various different formats for the text created by the command
\today, and also provides commands for displaying the current time (or
any given time), in 12-hour, 24-hour or text format. The package
overrides babel's date format, having its own library of date formats in
different languages. The package requires the fmtcount package. This
package is now obsolete and has been replaced by datetime2.

