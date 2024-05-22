function resetForm() {
    document.getElementById('playlist_id').value = '';
    document.getElementById('num_songs').value = '';

    var songListElement = document.getElementById('song-list');
    if (songListElement) {
        songListElement.innerHTML = '';
    }

    var analysisListElement = document.getElementById('analysis-list');
    if (analysisListElement) {
        analysisListElement.innerHTML = '';
    }

    var recommendedHeading = document.getElementById('recommended-heading');
    if (recommendedHeading) {
        recommendedHeading.remove();
    }

    var analysisHeading = document.getElementById('analysis-heading');
    if (analysisHeading) {
        analysisHeading.remove();
    }
}

document.getElementById('toggle-btn').addEventListener('click', function() {
    var sidebar = document.getElementById('sidebar');
    sidebar.classList.toggle('minimized');
});