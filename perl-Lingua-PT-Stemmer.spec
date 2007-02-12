#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Lingua
%define		pnam	PT-Stemmer
Summary:	Lingua::PT::Stemmer - Portuguese language stemming
Summary(pl.UTF-8):   Lingua::PT::Stemmer - określanie rdzeni słów w języku portugalskim
Name:		perl-Lingua-PT-Stemmer
Version:	0.01
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	74523d7da59dabbf561fa5cf60f98d02
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements a Portuguese stemming algorithm proposed in the
paper "A Stemming Algorithm for the Portuguese Language" by V. Moreira
and C. Huyck.

%description -l pl.UTF-8
Ten moduł zawiera implementację algorytmu określania rdzeni słów dla
języka portugalskiego zaproponowany w artykule V. Moreira'y i C Huycka
"A Stemming Algorithm for the Portuguese Language" ("Algorytm
określania rdzeni słów dla języka portugalskiego").

%package -n perl-Lingua-GL-Stemmer
Summary:	Lingua::GL::Stemmer - Galician language stemmer
Summary(pl.UTF-8):   Lingua::GL::Stemmer - określanie rdzeni słów w języku galicyjskim
Group:		Development/Languages/Perl

%description -n perl-Lingua-GL-Stemmer
Galician is an endangered language spoken in northwest region of
Spain. Galician is morphologically similar to Portuguese but phonetics
differs greatly. Due to the morphological similarity between
Portuguese and Galician, Portuguese stemming algorithm can be adopted
to stem Galician texts.

%description -n perl-Lingua-GL-Stemmer -l pl.UTF-8
Język galicyjski jest ginącym językiem, którym mówi się w północnej
Hiszpanii. Język galicyjski jest morfologicznie podobny do
portugalskiego lecz bardzo różni się wymową. Ze względu na
podobieństwo morfologiczne pomiędzy potrugalskim a galicyjskim, można
stosować dla języka galicyjskiego ten sam algorytm określania rdzeni
słów, co dla języka portugalskiego.

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
