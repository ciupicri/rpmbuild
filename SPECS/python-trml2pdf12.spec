%global srcname trml2pdf

Name:           python-trml2pdf12
Version:        1.2
Release:        13%{?dist}
Provides:       python-trml2pdf = %{version}-%{release}
Obsoletes:      python-trml2pdf <= 1.2-9
Summary:        Tiny RML2PDF is a tool to easily create PDF documents without programming

Group:          Development/Languages
License:        LGPLv2+
URL:            http://www.satchmoproject.com/snapshots/
Source0:        http://www.satchmoproject.com/snapshots/%{srcname}-%{version}.tar.gz
Source1:        http://svn.debian.org/viewsvn/python-modules/packages/python-trml2pdf/trunk/debian/%{srcname}.1?revision=2936&view=co#/%{srcname}.1

BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-setuptools
Requires:       python-reportlab >= 2.1
# Python-Imaging (PIL) if you use bitmap pictures
Requires:       python-imaging


%description
Convert Report Markup Language (RML) files to PDF.

This is a compatibility package for programs which still need version 1.2.


%prep
%setup -q -n %{srcname}-%{version}


%build
%{__python2} -c 'import setuptools; execfile("setup.py")' bdist_egg


%install
mkdir -p %{buildroot}%{python_sitelib}
easy_install -m --prefix %{buildroot}%{_usr} --always-unzip dist/*.egg

# copy man page
install -m 755 -d %{buildroot}%{_mandir}/man1
install -m 644 %{SOURCE1} %{buildroot}%{_mandir}/man1/trml2pdf12.1

# upsteam is a bit dead, so there's no one to extract a script from the module
chmod +x %{buildroot}%{python_sitelib}/TRML2PDF-1.0-py2.7.egg/trml2pdf/trml2pdf.py
install -m 755 -d %{buildroot}/%{_bindir}
ln -s %{python_sitelib}/TRML2PDF-1.0-py2.7.egg/trml2pdf/trml2pdf.py %{buildroot}%{_bindir}/trml2pdf12

 
%files
%doc COPYRIGHT.txt INSTALL.txt LICENSE.txt README.txt
%{python_sitelib}/*
%{_bindir}/*
%{_mandir}/*/*


%changelog
* Sun Oct 13 2013 Cristian Ciupitu <cristian.ciupitu@yahoo.com> - 1.2-13
- Fix misspell (thanks Jos de Kloe)

* Sun Oct 13 2013 Cristian Ciupitu <cristian.ciupitu@yahoo.com> - 1.2-12
- Replace __python macro with __python2 (thanks Jos de Kloe)

* Sun Oct 13 2013 Cristian Ciupitu <cristian.ciupitu@yahoo.com> - 1.2-11
- Use macros consistently (thanks Jos de Kloe)

* Thu Oct 10 2013 Cristian Ciupitu <cristian.ciupitu@yahoo.com> - 1.2-10
- Rename to python-trml2pdf12 (FPC #171)

* Thu Oct 10 2013 Cristian Ciupitu <cristian.ciupitu@yahoo.com> - 1.2-9
- Modernize SPEC (thanks Jason Tibbitts)

* Thu Oct 10 2013 Cristian Ciupitu <cristian.ciupitu@yahoo.com> - 1.2-8
- Fix URL for Source1 (thanks Jos de Kloe)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 09 2010 Cristian Ciupitu <cristian.ciupitu@yahoo.com> - 1.2-2
- Add man page (from Debian)

* Mon Nov 08 2010 Cristian Ciupitu <cristian.ciupitu@yahoo.com> - 1.2-1
- Initial package
