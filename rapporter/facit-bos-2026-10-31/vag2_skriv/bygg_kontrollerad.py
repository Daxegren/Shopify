#!/usr/bin/env python3
"""Bygger en skrivfil med bygg_m_skriv.py och kör sedan skrivfil_kontroll.py. Avslutar med kod 1 om kontrollen hittar FEL.
Användning: bygg_kontrollerad.py <namn> <utkastfiler,komma> <utlåtandefiler,komma> <utfil>
"""
import subprocess, sys, os
here = os.path.dirname(os.path.abspath(__file__))
kontroll = os.path.join(here, '..', '..', '..', 'shopify-sync', 'scripts', 'skrivfil_kontroll.py')
r = subprocess.run([sys.executable, os.path.join(here, 'bygg_m_skriv.py')] + sys.argv[1:5], cwd=here)
if r.returncode:
    sys.exit(r.returncode)
r = subprocess.run([sys.executable, kontroll, os.path.join(here, sys.argv[4])])
sys.exit(r.returncode)
