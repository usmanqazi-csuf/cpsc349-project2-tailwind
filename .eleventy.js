module.exports = function(eleventyConfig) {
    eleventyConfig.setUseGitIgnore(false);
    eleventyConfig.addPassthroughCopy("images");
    eleventyConfig.addPassthroughCopy("styles/main.css");
};
