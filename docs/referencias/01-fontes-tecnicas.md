# Fontes técnicas primárias

> Consulta/revisão: 2026-07-20. Links servem de base; versões usadas no código devem ser fixadas em lockfile/manifest.

## MusicXML

- W3C MusicXML 4.0: https://www.w3.org/2021/06/musicxml40/
- `<transpose>`: https://www.w3.org/2021/06/musicxml40/musicxml-reference/elements/transpose/
- `<diatonic>`: https://www.w3.org/2021/06/musicxml40/musicxml-reference/elements/diatonic/
- `<chromatic>`: https://www.w3.org/2021/06/musicxml40/musicxml-reference/elements/chromatic/
- `<octave-change>`: https://www.w3.org/2021/06/musicxml40/musicxml-reference/elements/octave-change/
- MXL/container: https://www.w3.org/2021/06/musicxml40/tutorial/compressed-mxl-files/

## Motor e ferramentas musicais

- music21 — intervalos: https://www.music21.org/music21docs/moduleReference/moduleInterval.html
- Audiveris — handbook: https://audiveris.github.io/audiveris/_pages/handbook/
- Audiveris — exportação MusicXML: https://audiveris.github.io/audiveris/_pages/guides/advanced/export/
- MuseScore Studio — command line: https://handbook.musescore.org/appendix/command-line-usage

A presença de uma ferramenta nesta lista não é decisão de produção; consultar `../00-visao-geral/09-decisoes-pendentes.md`.

## Backend e filas

- FastAPI — UploadFile: https://fastapi.tiangolo.com/tutorial/request-files/
- Celery — tasks: https://docs.celeryq.dev/en/stable/userguide/tasks.html
- Celery — workers: https://docs.celeryq.dev/en/stable/userguide/workers.html

## Segurança

- OWASP File Upload Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html
- OWASP XML Security Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/XML_Security_Cheat_Sheet.html
- OWASP XXE Prevention Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html
- OWASP IDOR Prevention Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Insecure_Direct_Object_Reference_Prevention_Cheat_Sheet.html
- OWASP Session Management Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html
- OWASP Logging Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html
- OWASP Docker Security Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html
- OWASP Web Service Security Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Web_Service_Security_Cheat_Sheet.html


## Frontend, design system e acessibilidade

- Next.js App Router: https://nextjs.org/docs/app
- Next.js project structure: https://nextjs.org/docs/app/getting-started/project-structure
- Next.js font optimization: https://nextjs.org/docs/app/getting-started/fonts
- Next.js lazy loading: https://nextjs.org/docs/app/guides/lazy-loading
- Tailwind CSS theme variables: https://tailwindcss.com/docs/theme
- Tailwind CSS responsive design e container queries: https://tailwindcss.com/docs/responsive-design
- shadcn/ui theming: https://ui.shadcn.com/docs/theming
- shadcn/ui components: https://ui.shadcn.com/docs/components
- WCAG 2.2: https://www.w3.org/TR/WCAG22/
- View Transition API: https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API
- Storybook accessibility testing: https://storybook.js.org/docs/writing-tests/accessibility-testing
- Storybook UI testing: https://storybook.js.org/docs/writing-tests
- Core Web Vitals thresholds: https://web.dev/articles/defining-core-web-vitals-thresholds
- Motion for React: https://motion.dev/docs/react
- Motion SVG animation: https://motion.dev/docs/react-svg-animation
- Motion reduced motion: https://motion.dev/docs/react-use-reduced-motion
- GSAP docs: https://gsap.com/docs/v3/
- GSAP com React e `useGSAP`: https://gsap.com/resources/React/
- GSAP MotionPathPlugin: https://gsap.com/docs/v3/Plugins/MotionPathPlugin/
- GSAP DrawSVGPlugin: https://gsap.com/docs/v3/Plugins/DrawSVGPlugin/
- GSAP pricing/licença: https://gsap.com/pricing/
- Anime.js timelines: https://animejs.com/documentation/timeline/
- Anime.js SVG utilities: https://animejs.com/documentation/svg/
- React Spring: https://www.react-spring.dev/

## Regra de uso

Ao implementar, registrar a versão exata da especificação, biblioteca e engine. Mudança de versão em parser/OMR/renderer exige executar corpus funcional e hostil antes de release.
