#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Lingua
%define	pnam	PT-Stemmer
Summary:	Lingua::PT::Stemmer - Portuguese language stemming
Summary(pl):	Lingua::PT::Stemmer - okre¶lanie rdzeni s³ów w jêzyku portugalskim
Name:		perl-Lingua-PT-Stemmer
Version:	0.01
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	74523d7da59dabbf561fa5cf60f98d02
BuildRequires:	perl >= 5.8
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements a Portuguese stemming algorithm proposed in the
paper "A Stemming Algorithm for the Portuguese Language" by V. Moreira
and C. Huyck.

%description -l pl
Ten modu³ zawiera implementacjê algorytmu okre¶lania rdzeni s³ów dla
jêzyka portugalskiego zaproponowany w artykule V. Moreira'y i C Huycka
"A Stemming Algorithm for the Portuguese Language" ("Algorytm
okre¶lania rdzeni s³ów dla jêzyka portugalskiego").

%package -n perl-Lingua-GL-Stemmer
Summary:	Lingua::GL::Stemmer - Galician language stemmer
Summary(pl):	Lingua::GL::Stemmer - okre¶lanie rdzeni s³ów w jêzyku galicyjskim
Group:		Development/Languages/Perl

%description -n perl-Lingua-GL-Stemmer
Galician is an endangered language spoken in northwest region of
Spain. Galician is morphologically similar to Portuguese but phonetics
differs greatly. Due to the morphological similarity between
Portuguese and Galician, Portuguese stemming algorithm can be adopted
to stem Galician texts.

%description -n perl-Lingua-GL-Stemmer -l pl
Jêzyk galicyjski jest gin±cym jêzykiem, którym mówi siê w pó³nocnej
Hiszpanii. Jêzyk galicyjski jest morfologicznie podobny do
portugalskiego lecz bardzo ró¿ni siê wymow±. Ze wzglêdu na
podobieñstwo morfologiczne pomiêdzy potrugalskim a galicyjskim, mo¿na
stosowaæ dla jêzyka galicyjskiego ten sam algorytm okre¶lania rdzeni
s³ów, co dla jêzyka portugalskiego.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Lingua/PT
%{_mandir}/man3/*PT*

%files -n perl-Lingua-GL-Stemmer
%defattr(644,root,root,755)
%{perl_vendorlib}/Lingua/GL
%{_mandir}/man3/*GL*
