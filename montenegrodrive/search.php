<?php
/**
 * Search results template
 *
 * @package MontenegroDrive
 */

if ( ! defined( 'ABSPATH' ) ) { exit; }

get_header();
?>

<div class="max-w-container-max mx-auto px-gutter py-section-padding">

    <header class="mb-stack-lg">
        <h1 class="font-h1 text-h1 text-primary">
            <?php
            printf(
                /* translators: %s: search query */
                esc_html__( 'Search results for: %s', 'montenegrodrive' ),
                '<span class="text-brand-accent">' . esc_html( get_search_query() ) . '</span>'
            );
            ?>
        </h1>
    </header>

    <?php if ( have_posts() ) : ?>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-stack-lg">
            <?php while ( have_posts() ) : the_post(); ?>
                <article id="post-<?php the_ID(); ?>" <?php post_class( 'bg-surface-container-lowest rounded-xl overflow-hidden shadow-sm hover:shadow-md transition-all' ); ?>>
                    <?php if ( has_post_thumbnail() ) : ?>
                        <a href="<?php the_permalink(); ?>" class="block aspect-[4/3] overflow-hidden">
                            <?php the_post_thumbnail( 'large', array( 'class' => 'w-full h-full object-cover hover:scale-105 transition-transform duration-500' ) ); ?>
                        </a>
                    <?php endif; ?>
                    <div class="p-6">
                        <h2 class="font-h3 text-h3 mb-2">
                            <a class="text-primary hover:text-primary-container" href="<?php the_permalink(); ?>"><?php the_title(); ?></a>
                        </h2>
                        <div class="text-on-surface-variant"><?php the_excerpt(); ?></div>
                    </div>
                </article>
            <?php endwhile; ?>
        </div>

        <div class="mt-stack-lg">
            <?php the_posts_pagination(); ?>
        </div>

    <?php else : ?>

        <div class="text-center py-section-padding">
            <p class="font-body-lg text-secondary mb-stack-md">
                <?php esc_html_e( 'No results found. Try a different search.', 'montenegrodrive' ); ?>
            </p>
            <?php get_search_form(); ?>
        </div>

    <?php endif; ?>

</div>

<?php get_footer();
