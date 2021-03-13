# generated by cabal-rpm-2.0.6
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

Name:           cabal-install
Version:        3.0.0.0
Release:        6%{?dist}
Summary:        The command-line interface for Cabal and Hackage

License:        BSD
Url:            https://hackage.haskell.org/package/%{name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
# End cabal-rpm sources
Source10:       cabal-install.sh

# Begin cabal-rpm deps:
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-Cabal-static
BuildRequires:  ghc-HTTP-static
BuildRequires:  ghc-array-static
BuildRequires:  ghc-async-static
BuildRequires:  ghc-base-static
BuildRequires:  ghc-base16-bytestring-static
BuildRequires:  ghc-binary-static
BuildRequires:  ghc-bytestring-static
BuildRequires:  ghc-containers-static
BuildRequires:  ghc-cryptohash-sha256-static
BuildRequires:  ghc-deepseq-static
BuildRequires:  ghc-directory-static
BuildRequires:  ghc-echo-static
BuildRequires:  ghc-edit-distance-static
BuildRequires:  ghc-filepath-static
BuildRequires:  ghc-hackage-security-static
BuildRequires:  ghc-hashable-static
BuildRequires:  ghc-mtl-static
BuildRequires:  ghc-network-static
BuildRequires:  ghc-network-uri-static
BuildRequires:  ghc-parsec-static
BuildRequires:  ghc-pretty-static
BuildRequires:  ghc-process-static
BuildRequires:  ghc-random-static
BuildRequires:  ghc-resolv-static
BuildRequires:  ghc-stm-static
BuildRequires:  ghc-tar-static
BuildRequires:  ghc-text-static
BuildRequires:  ghc-time-static
BuildRequires:  ghc-unix-static
BuildRequires:  ghc-zlib-static
# End cabal-rpm deps

# cabal-install 2.0 does not require Cabal
Requires:       ghc-compiler
# for /etc/bash_completion.d/
Requires:       filesystem
# nslookup used for mirror dns
Requires:       bind-utils
# for /etc/profile.d/
Requires:       setup
Recommends:     ghc
# added for F26
Obsoletes:      %{name}-common < %{version}-%{release}
Obsoletes:      %{name}-static < %{version}-%{release}

%description
The 'cabal' command-line program simplifies the process of managing Haskell
software by automating the fetching, configuration, compilation and
installation of Haskell libraries and programs.


%prep
# Begin cabal-rpm setup:
%setup -q
chmod a-x README.md changelog
# End cabal-rpm setup

%build
# Begin cabal-rpm build:
%ghc_bin_build
# End cabal-rpm build


%install
# Begin cabal-rpm install
%ghc_bin_install
# End cabal-rpm install

install -pm 644 -D -t %{buildroot}%{_datadir}/bash-completion/completions/ bash-completion/cabal

install -pm 644 -D -t %{buildroot}%{_sysconfdir}/profile.d/ %{SOURCE10}


%files
# Begin cabal-rpm files:
%license LICENSE
%doc README.md changelog
%{_bindir}/cabal
# End cabal-rpm files
%config(noreplace) %{_sysconfdir}/profile.d/cabal-install.sh
%{_datadir}/bash-completion/completions/cabal
%{_mandir}/man1/cabal.1*


%changelog
* Sat Mar 13 2021 Marko Kungla <marko.kungla@gmail.com> 3.0.0.0-6
- remove patches

* Sat Mar 13 2021 Marko Kungla <marko.kungla@gmail.com> 3.0.0.0-5
- new package built with tito

* Sat Mar 13 2021 Marko Kungla <marko.kungla@gmail.com> 3.0.0.0-4
- new package built with tito

* Sat Mar 13 2021 Marko Kungla <marko.kungla@gmail.com> 3.0.0.0-4
- new package built with tito

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 12 2020 Jens Petersen <petersen@redhat.com> - 3.0.0.0-3
- Recommends ghc (thanks Tristan de Cacqueray,#1)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 07 2020 Jens Petersen <petersen@redhat.com> - 3.0.0.0-1
- update to 3.0.0.0

* Tue Apr 14 2020 Jens Petersen <petersen@redhat.com> - 2.4.1.0-2
- backport new-sdist upstream fix for doc file permissions
  (https://github.com/haskell/cabal/issues/5813)

* Sun Feb 09 2020 Jens Petersen <petersen@redhat.com> - 2.4.1.0-1
- update to 2.4.1.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Jens Petersen <petersen@redhat.com> - 2.4.1.0-1
- update to 2.4.1.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May  9 2019 fedora-toolbox <petersen@redhat.com> - 2.2.0.0-3
- rebuild

* Tue Apr  9 2019 Jens Petersen <petersen@redhat.com> - 2.2.0.0-2
- resolv is now packaged

* Thu Feb 21 2019 Jens Petersen <petersen@redhat.com> - 2.2.0.0-1
- update to 2.2.0.0
- subpackage resolv dep
- install bash-completion file under datadir (Chris King-Parra, #1683879)

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 2.0.0.1-12
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 14 2018 Jens Petersen <petersen@redhat.com> - 2.0.0.1-10
- drop the rpmlint whitelist of ghc-Cabal-devel again since no longer Requires

* Thu Nov 22 2018 Jens Petersen <petersen@redhat.com> - 2.0.0.1-9
- require bind-utils for nslookup used for secure mirror dns lookup

* Wed Nov 21 2018 Jens Petersen <petersen@redhat.com> - 2.0.0.1-8
- no longer requires ghc-Cabal-devel

* Fri Oct  5 2018 Jens Petersen <petersen@redhat.com> - 2.0.0.1-7
- rebuild

* Fri Oct  5 2018 Jens Petersen <petersen@redhat.com> - 2.0.0.1-6
- link cabal statically to its Haskell deps for ghc modules portability

* Sat Jul 28 2018 Jens Petersen <petersen@redhat.com> - 2.0.0.1-5
- revise .cabal

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 23 2018 Jens Petersen <petersen@redhat.com> - 2.0.0.1-3
- unbundle echo library

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Jens Petersen <petersen@redhat.com> - 2.0.0.1-1
- update to 2.0.0.1
- subpackage new echo dep

* Sat Oct 21 2017 Jens Petersen <petersen@fedoraproject.org> - 1.24.0.2-6
- the bundled libraries are now packaged in Fedora

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 24 2017 Jens Petersen <petersen@redhat.com> - 1.24.0.2-3
- set manpage permission to 0644

* Wed Apr 26 2017 Jens Petersen <petersen@redhat.com> - 1.24.0.2-2
- requires ghc-Cabal-devel (Matej Smid, #1445210)

* Wed Feb 22 2017 Jens Petersen <petersen@redhat.com> - 1.24.0.2-1
- update to 1.24.0.2

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 21 2017 Jens Petersen <petersen@redhat.com> - 1.22.9.0-2
- drop static and common subpackages

* Sun Jun 26 2016 Jens Petersen <petersen@redhat.com> - 1.22.9.0-1
- update to 1.22.9.0

* Mon Jun  6 2016 Jens Petersen <petersen@redhat.com> - 1.22.6.0-1
- update to 1.22.6.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 13 2015 Jens Petersen <petersen@redhat.com> - 1.18.1.0-1
- security version update for upload command

* Thu Apr  2 2015 Jens Petersen <petersen@redhat.com> - 1.18.0.8-1
- update to 1.18.0.8

* Thu Aug  7 2014 Jens Petersen <petersen@redhat.com> - 1.18.0.5-1
- update to 1.18.0.5
- obsolete cabal-dev
- add static and common subpackages

* Tue Jul  8 2014 Jens Petersen <petersen@redhat.com> - 1.16.0.2-35
- f21 rebuild

* Fri Apr 18 2014 Jens Petersen <petersen@redhat.com> - 1.16.0.2-34
- bump release over haskell-platform

* Thu Apr 17 2014 Jens Petersen <petersen@redhat.com> - 1.16.0.2-32
- mark bash_completion.d and profile.d files as config (#1069062)
- require filesystem and setup to own the sysconfig dirs (#1069062)

* Mon Feb 24 2014 Jens Petersen <petersen@redhat.com> - 1.16.0.2-31
- update to 1.16.0.2
- split out of haskell-platform (#1069062)
- only show cabal-install upgrade notice for verbose

* Tue May  8 2012 Jens Petersen <petersen@redhat.com> - 0.14.0-1
- update to 0.14.0 release

* Tue Mar 20 2012 Jens Petersen <petersen@redhat.com> - 0.13.3-0.1
- update to latest darcs

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 28 2011 Jens Petersen <petersen@redhat.com> - 0.10.2-6
- rebuild for haskell-platform-2011.4.0.0

* Fri Dec 16 2011 Jens Petersen <petersen@redhat.com> - 0.10.2-5
- bring back requires ghc-compiler (Stanislav Ochotnicky, #760461)

* Thu Oct 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.10.2-4.2
- rebuild with new gmp without compat lib

* Mon Oct 10 2011 Peter Schiffer <pschiffe@redhat.com> - 0.10.2-4.1
- rebuild with new gmp

* Tue Jun 21 2011 Jens Petersen <petersen@redhat.com> - 0.10.2-4
- ghc_arches replaces ghc_excluded_archs

* Mon Jun 20 2011 Jens Petersen <petersen@redhat.com> - 0.10.2-3
- BR ghc-Cabal-devel and use ghc_excluded_archs
- drop ghc requires to allow local ghc

* Wed May 25 2011 Jens Petersen <petersen@redhat.com> - 0.10.2-2
- add ppc64

* Fri Mar 11 2011 Jens Petersen <petersen@redhat.com> - 0.10.2-1
- update to 0.10.2

* Thu Mar 10 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 0.9.6-0.2
- Enable build on sparcv9

* Tue Feb 15 2011 Jens Petersen <petersen@redhat.com> - 0.9.6-0.1
- update to 0.9.6 pre snapshot

* Tue Feb 15 2011 Jens Petersen <petersen@redhat.com> - 0.9.5-0.5
- rebuild for haskell-platform-2011.1 updates

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 23 2011 Jens Petersen <petersen@redhat.com> - 0.9.5-0.3
- update to cabal2spec-0.22.4
- BR ghc-devel

* Sun Dec  5 2010 Jens Petersen <petersen@redhat.com> - 0.9.5-0.2
- rebuild with HTTP-4000.1.1

* Thu Nov 25 2010 Jens Petersen <petersen@redhat.com> - 0.9.5-0.1
- update to current 0.9.5 snapshot

* Fri Jul 16 2010 Jens Petersen <petersen@redhat.com> - 0.8.2-1
- update to 0.8.2 for haskell-platform-2010.2.0.0

* Sun Jun 27 2010 Jens Petersen <petersen@redhat.com> - 0.8.0-5
- sync cabal2spec-0.22.1

* Wed May 19 2010 Jens Petersen <petersen@redhat.com> - 0.8.0-4
- append ~/.cabal/bin to PATH (if dir exists) with new
  /etc/profile.d/cabal-install.sh (#509699)

* Tue Apr 27 2010 Jens Petersen <petersen@redhat.com> - 0.8.0-3
- rebuild against ghc-6.12.2

* Tue Mar 23 2010 Jens Petersen <petersen@redhat.com> - 0.8.0-2
- rebuild against HTTP-4000.0.9 for haskell-platform-2010.1.0.0

* Mon Jan 11 2010 Jens Petersen <petersen@redhat.com> - 0.8.0-1
- update to 0.8.0 for ghc-6.12.1
- add dynamic bcond
- drop redundant buildroot and its install cleaning

* Wed Sep 16 2009 Jens Petersen <petersen@redhat.com> - 0.6.2-6
- really rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 17 2009 Jens Petersen <petersen@redhat.com> - 0.6.2-4
- buildrequires ghc-rpm-macros (cabal-0.16)

* Sun Apr 26 2009 Jens Petersen <petersen@redhat.com> - 0.6.2-3
- rebuild against ghc-6.10.2

* Fri Feb 27 2009 Jens Petersen <petersen@redhat.com> - 0.6.2-2
- update for cabal2spec-0.11:
- use global
- fix source url
- add ix86 and alpha archs

* Mon Feb 23 2009 Jens Petersen <petersen@redhat.com> - 0.6.2-1
- update to 0.6.2 release

* Mon Feb  9 2009 Jens Petersen <petersen@redhat.com> - 0.6.0-3
- fix source url

* Wed Jan  7 2009 Jens Petersen <petersen@redhat.com> - 0.6.0-2
- add bash completion file
- update cabal build macro

* Tue Nov 11 2008 Jens Petersen <petersen@redhat.com> - 0.6.0-1
- initial package for Fedora
