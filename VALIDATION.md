# Validation

Initial release: browser automation was run against the standalone HTML in Chromium. All 17 baseline checks passed, with no uncaught browser errors in the tested flows:

1. All 26 required muscle entries map to selectable 3D geometry.
2. Deep view, isolation, and posterior orientation work.
3. Harmless spelling errors are accepted while a different structure is rejected.
4. Incorrect identification is scored once and enters the review queue.
5. Action/function answers use self-assessment and a separate progress record.
6. Mock practical feedback and scoring remain hidden until submission; pending answers can then be assessed.
7. The station timer submits unanswered responses and completes safely.
8. Reflex-arc ordering grades the actual selected order.
9. Diagram pin selection records the chosen structure.
10. Matching uses an action cue without revealing the highlighted answer.
11. Uploaded lab photographs store a normalized quiz pin.
12. Progress and photographs survive refresh.
13. Backup export/import restores progress and photographs exactly.
14. The session builder creates the requested number of stations and covers all selected units.
15. Dashboard and study layouts fit a 390px mobile viewport.
16. Storage failure is disclosed, and WebGL failure displays the embedded image reference.
17. No uncaught browser errors occurred in the tested flows.

Desktop study screens, cranial nerve and brain pins, mobile layout, and representative superficial/deep 3D selections were also visually reviewed. This verifies the tested app behavior; it is not an independent instructor review of the anatomy answer key or a guarantee of an exam score.

## Revision 1.1: anatomy context and camera selection

All 16 targeted browser checks passed after the update:

1. A required muscle is selectable in the rotated posterior view.
2. Canvas selection changes the selected muscle.
3. Canvas selection preserves camera rotation, pan, zoom and view mode.
4. Catalog selection preserves the same camera pose.
5. Toggling the label preserves the camera pose.
6. Added reference anatomy has visible surfaces.
7. Clicking added context selects no muscle and leaves the view unchanged.
8. All added context geometry is outside the selectable muscle IDs.
9. The viewer explicitly marks surrounding anatomy as reference only.
10. Focus muscle recenters intentionally while preserving the viewing direction.
11. Selection also preserves isolate mode.
12. Reset still deliberately restores the default selected-muscle view.
13. Quiz hints preserve the station camera pose.
14. Answer feedback preserves the station camera pose.
15. Added controls fit the mobile viewport.
16. No uncaught browser errors during the updated flows.

A byte comparison confirms that `content.json` is unchanged from the initial release: 123 study cards and 26 selectable muscle entries/groups. The progress storage key and backup schema are unchanged. The updated face, full body and side views were visually reviewed. Registration is approximate and the added anatomy is reference only.

## Revision 1.2: GitHub Pages and phone access

Verified using a local HTTP server with both a site root and a GitHub-style project subpath. All 16 targeted checks passed:

1. GitHub project subpath loads the app with all 123 cards and 26 selectable muscles.
2. Mobile dashboard fits a 390px viewport.
3. Manifest resolves within the repository subpath.
4. Phone icon 192x192 is served.
5. Phone icon 512x512 is served.
6. Service worker controls only the GitHub project subpath.
7. Mobile study layout also fits the viewport.
8. Study progress saves before offline use.
9. Offline reload restores the full 3D app.
10. Saved progress survives offline reload.
11. Camera selection fix also works offline on the hosted build.
12. The same package also runs at a site root.
13. Root and project deployments keep separate scoped offline caches.
14. Root deployment does not replace the project worker.
15. Core app loading makes no external CDN requests.
16. No uncaught errors in hosted mobile and offline flows.

The phone checks use Chromium mobile emulation with touch input at 390 × 844, including an assertion that the document fits the actual 390px width. A grid sizing fix prevents the 3D canvas from expanding the layout. Offline reload, retained progress, installation assets and cache isolation were tested. This is local deployment validation; an actual GitHub deployment and physical iPhone/Android installation have not been performed.
